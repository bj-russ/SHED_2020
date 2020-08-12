from maq20 import MAQ20Module
import maq20.utilities as utils


class ISOx(MAQ20Module):
    """
    MAQ20-ISOx class definition.

    Contains functions that are specific to the ISO.
    """

    BURST_MAX_VALUE = 0x01FFFFFF  # 33554431
    MAX_NUMBER_OF_REGS = 100

    def __init__(self, maq20_module):
        """
        :param maq20_module: pass in the module returned by MAQ20.get_module_list()
        """
        if isinstance(maq20_module, MAQ20Module):
            super(ISOx, self).__init__(com=maq20_module.get_com_module(),
                                       registration_number=maq20_module.get_registration_number())
            self._scan_list = []
            self._index_scan_list = 0
            self._buffer_size = 100
            self.read_scan_list()
        else:
            raise RuntimeError('Passed in object is not MAQ20 object.')

    def name_change(self, name: str):
        if len(name) < 15:
            spaces_needed = 15 - len(name)
            for i in range(spaces_needed):
                name += " "
        self.write_registers(0, name)

    def _next_scan_list_item(self):
        """
        Utility function used by the Burst mode related functions.
        :return: the next index to be read for the Burst mode.
        """
        result = self._scan_list[self._index_scan_list]
        if result == 0xFF:
            self._index_scan_list = 0
            result = self._scan_list[self._index_scan_list]
            if result == 0xFF:
                self._index_scan_list += 1
                return 0
            else:
                self._index_scan_list += 1
                return result
        else:
            self._index_scan_list += 1
            return result

    def read_scan_list(self):
        self._scan_list = self.read_registers(600, 10)
        return self._scan_list

    def write_scan_list(self, scan_list):
        """
        Writes a new Burst mode scan list to the Iso module.
        :param scan_list: a list(int) with int -> [0, ..., 7]
        :return: modbus response
        """
        if len(scan_list) < 11:
            scan_list.append(0xFF)
        self._index_scan_list = 0
        return self.write_registers(600, scan_list)

    def write_burst_mode_size(self, size):
        """
        Writes a new burst mode size measured in number of samples.
        MAX value is: 33554431
        :param size: int
        :return: False if failed, True if succeeds.
        """
        if size > ISOx.BURST_MAX_VALUE:
            return False
        else:
            msb = size >> 16
            lsb = size & 0x0000FFFF
            self.write_register(670, msb)
            self.write_register(671, lsb)
            self._buffer_size = size
            return True

    def read_burst_mode_size(self):
        """
        :return: burst mode size currently in ivi's RAM
        """
        msb = self.read_register(670)
        lsb = self.read_register(671)
        return (msb << 16) | (lsb & 0xFFFF)

    def write_burst_enable(self, enable):
        """
        Enable or disable the burst mode in ISO module, this starts the burst mode sampling.
        :param enable: bool
        :return: modbus response.
        """
        return self.write_register(1200, enable)

    def write_burst_busy(self):
        return self.read_register(1202)

    def write_burst_read(self, wait=True):
        """
        Reads burst mode data from the ISO module.
        :param wait: if wait is True then this function will wait until the IVI has finished sampling.
        :param wait: if wait is False then host will start reading. This means that the returned value length
                     is not guaranteed to be equal to burst mode size.
        :return: a list of lists defined by the scan list. default scan list is [1,2,3,4,5,6,7,0xFF,0xFF]
        """
        # Make the result structure.
        result = self._make_result_dict_for_burst_mode()

        # Poll the module to see if finished, it parameter wait is true then program will stall until finished.
        self._wait(wait)

        # Start reading burst mode result.
        number_of_max_reads = self._buffer_size / ISOx.MAX_NUMBER_OF_REGS
        for i in range(int(number_of_max_reads)):
            max_read = self.read_registers(1201, ISOx.MAX_NUMBER_OF_REGS)
            for regs in range(ISOx.MAX_NUMBER_OF_REGS):
                if max_read[regs] == 32767:
                    return result
                index = self._next_scan_list_item()
                result[index].append(self._channel_counts_to_eng(index, max_read[regs]))
        while True:
            data_read = self.read_registers(1201, 1)
            if data_read[0] == 32767:
                return result
            index = self._next_scan_list_item()
            data_read = self._channel_counts_to_eng(index, data_read[0])
            result[index].append(data_read)

    def _make_result_dict_for_burst_mode(self):
        """
        Makes a dictionary that has keys of the channel index existing in the scan list of this module.
        example for scan list = [0, 0, 1, 6, 6, 7]
        {
            0: [],
            1: [],
            6: [],
            7: [],
        }
        :return:
        """
        result = {}
        channels = []
        for index in self._scan_list:
            if index == 0xFF:
                break
            found = False
            for channel in channels:
                if index == channel:
                    found = True
            if not found:
                channels.append(index)
                result[index] = []
        return result

    def _wait(self, wait):
        import time
        slept = 0
        while self.write_burst_busy() and wait:
            # print("Time waiting: " + str(slept) + " seconds.")
            time.sleep(1)
            slept += 1
        # print("Started Reading...")
