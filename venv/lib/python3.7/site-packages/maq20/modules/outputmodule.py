from maq20.maq20module import MAQ20Module
import maq20.utilities as utils


class OutputModule(MAQ20Module):

    def __init__(self, maq20_module):
        if isinstance(maq20_module, MAQ20Module):
            super(OutputModule, self).__init__(com=maq20_module.get_com_module(),
                                               registration_number=maq20_module.get_registration_number())
        else:
            raise RuntimeError('Passed in object is not MAQ20 object.')

    ################################
    # Module Configuration [100,499]
    ################################

    def read_output_range(self, channel=0):
        """
        Range for each of 8 channels
        :param channel: channel to be read.
        :return: integer.
        """
        return self.read_register(100+channel)

    def write_output_range(self, channel, value):
        """
        Range for each of 8 channels
        :param value: value to be written
        :param channel: channel to be used
        :return: modbus response
        """
        return self.write_register(100+channel, value)

    def read_default_output(self, channel=0):
        """
        Default Output for each channel
        :param channel: channel to be read.
        :return: int
        """
        return self.read_register(110+channel)

    def write_default_output(self, channel, value):
        """
        Default Output for each channel
        :param value: value to be written.
        :param channel: channel to be used.
        :return: modbus response.
        """
        return self.write_register(110+channel, value)

    def write_save_module_configuration_to_eeprom(self, value):
        """
        0 = Range, 1 = Default Output
        :param value: 0 or 1
        :return: modbus response
        """
        return self.write_register(119, value)

    ###############################
    # Burst Mode Settings [600,999]
    ###############################

    def read_burst_mode_control(self):
        """
        1 = Start Burst, 0 = Stop Burst
        :return: 0 or 1
        """
        return self.read_register(600)

    def read_refresh_rate(self):
        """
        milliseconds up to 2^16
        :return: int
        """
        return self.read_register(601)

    def read_number_of_channels_with_burst_active(self):
        """
        Number of sequential channels starting with Ch 0.  i.e. 3 = Ch 0, Ch1, Ch 2 active.
        :return: int
        """
        return self.read_register(602)

    def write_save_refresh_rate_to_eeprom(self):
        """
        Saves refresh rate and number of channels with burst active to EEPROM.
        :return: modbus response.
        """
        return self.write_register(609, 0)

    def read_burst_data_pointer(self, channel=0):
        """
        Data pointer for each channel
        :param channel: channel to be read.
        :return: integer.
        """
        return self.read_register(610+channel) if channel < self._number_of_channels else None

    def write_save_burst_data_to_eeprom(self, channel=0):
        """
        Save burst data to EEPROM.
        :param channel: channel to be saved.
        :return: modbus response.
        """
        return self.write_register(619, channel) if channel < self._number_of_channels else None

    def read_burst_data(self, channel=0):
        """
        Store up to 100 data points per channel in memory.  When Burst Mode is active, data is output sequentially to
        active channels at the specified refresh rate in a single sequence or continuously looped.  Write or read up
        to 10 data points at a time to or from a channel allocated memory space by first setting the Burst Data Pointer
        and then writing the data points to the Start Address for the channel (i.e. address 620 for Channel 0).  Save
        data to EEPROM by writing a 0 to register 619.
        :param channel: channel to be read.
        :return: integer.
        """
        return self.read_registers(620+(channel*10), 10)
