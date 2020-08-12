from maq20.maq20module import MAQ20Module
from maq20.maq20com import COMx
from ftplib import FTP

RESET_STANDARD = 0
RESET_DEFAULT = 0


class MAQ20:
    """"
    MAQ20 System
    A class that provides easy to use high level functions for MAQ20 Modules.
    """

    def __init__(self, ip_address="192.168.128.100", port=502):
        """
        Initializes the MAQ20 with the given input parameters.
        :param ip_address: a string containing the ip address of the MAQ20, default is 192.168.128.100
        :param port: default is 502
        """
        self._com = None  # type: COMx
        self._ip_address = ip_address
        self._port = port
        self._username = ''
        self._password = ''
        self._com = COMx(ip_address, port)
        self._module_list = []  # type: list[MAQ20Module]
        self.scan_module_list()
        self._iter_index = 0

    def read_register(self, address):
        """
        Low level register access.
        Performs a modbus read register request to the MAQ20
        :param address: requested address
        :return: int - [-32767, 32767]
        """
        return self._com.read_register(address)

    def read_registers(self, address, number_of_registers):
        """
        Low level register access.
        Performs a modbus read registers request to the MAQ20
        :param address: starting address.
        :param number_of_registers: number of registers to be read in sequence.
        :return: list(int) [-32767, 32767]
        """
        return self._com.read_registers(address, number_of_registers)

    def write_register(self, address, value):
        """
        Low level register access.
        Performs a modbus write register request to the MAQ20
        :param address: starting address.
        :param value: int [-32767, 32767] or a str of size 1
        :return: modbus response.
        """
        return self._com.write_register(address, value)

    def write_registers(self, address, values=None):
        """
        Low level register access.
        Performs a modbus write registers request to the MAQ20
        :param address: starting address.
        :param values: list(int) [-32767, 32767] or a str
        :return: modbus response.
        """
        return self.read_registers(address, values)

    def scan_module_list(self):
        """
        Refreshes the internal list of registered modules in a system.
        To get the list call function: get_module_list()
        """
        module_list = [self._com]  # type: list[MAQ20Module]
        modules_present = self._com.read_module_status()
        for i in range(1, len(modules_present)):
            if modules_present[i]:
                module_list.append(MAQ20Module(com=self._com, registration_number=i))
        self._module_list = module_list

    def get_system_information(self):
        """
        :return: a string containing information about every registered module in the system.
        """
        result_str = ""
        for a_module in self._module_list:
            result_str += a_module.module_information() + "\n"
        return result_str

    def get_module(self, registration_number):
        """
        Returns the MAQ20Module with the registration number requested.
        :param registration_number: int, 0 to 23
        :return: MAQ20Module
        """
        return self._module_list[registration_number]

    def get_module_list(self):
        """
        :return: the current module list that the MAQ20 object holds
        note: This does not refresh the list of registered modules.
        """
        return self._module_list

    def read_system_data(self):
        """
        Read every channel in every module
        :return: a list of lists containing the values read.
        """
        result = []
        for a_module in self._module_list[1:]:
            result.append(a_module.read_data(start_channel=0,
                                             number_of_channels=a_module.get_number_of_channels()))
        return result

    def print_system_data(self):
        """
        Prints system data to the console
        :return: None
        """
        data = self.read_system_data()
        i = 0
        for a_module in self._module_list[1:]:
            print(str(a_module .get_registration_number()) + ": " + a_module .get_name() + "= " + str(data[i]))
            i += 1

    def get_com(self):
        """
        :return: MAQ20COM currently registered in this system. 
        """
        return self._com

    def read_data(self, a_module=1, channel=0):
        """
        Calls the read_data() function registered at a_module index.
        :param a_module: int, 0 to 23
        :param channel: int, 0 and greater.
        :return: list
        """
        return self._module_list[a_module].read_data(start_channel=channel, number_of_channels=1)

    def find(self, name_or_sn: str=None):
        """
        Attempts to find a MAmodule by name or serial number.
        :param name_or_sn: a string that contains a partial name or full serial number.
        :return: Return a MAQ20Module reference to the module found or None if not found.
        """
        # name_or_sn.upper()
        result = None
        if type(name_or_sn) is str:
            for a_module in self._module_list:
                module_name = a_module .get_name()
                sn = a_module .get_serial_number()
                if module_name.find(name_or_sn) > -1 or name_or_sn == sn:
                    result = a_module
                    break
        return result

    def time(self) -> str:
        """
        returns the time read from the module in a human readable form.
        :return: str
        """
        time_info = self._com.read_registers(1200, 7)
        return "20{0[6]}/{0[5]}/{0[4]} - {1} - {0[2]:02}.{0[1]:02}.{0[0]:02}".format(time_info, {
            1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday",
        }[time_info[3]])

    # FTP functions.

    def ftp_login(self, username='maq20', password='1234'):
        self._username = username
        self._password = password

    def ftp_dir(self):
        if self._com.read_card_available():
            with FTP(self._ip_address) as ftp:
                catcher = self.StdoutCatcher()
                ftp.login(user=self._username, passwd=self._password)
                ftp.dir()
                result = catcher.get_text()
            return result
        else:
            return 'SD card not inserted.'

    def ftp_get(self, filename: str):
        if self._com.read_card_available():
            with FTP(self._ip_address) as ftp:
                ftp.login(user=self._username, passwd=self._password)
                with open(filename, 'wb') as local_file:
                    result = ftp.retrbinary('RETR {}'.format(filename.upper()), local_file.write)
            return result
        else:
            return 'SD card not inserted.'

    def ftp_del(self, filename: str):
        if self._com.read_card_available():
            with FTP(self._ip_address) as ftp:
                ftp.login(user=self._username, passwd=self._password)
                result = ftp.delete(filename)
            return result
        else:
            return 'SD card not inserted.'

    def ftp_filenames(self):
        result = []
        response = self.ftp_dir().split('\n')
        for line in response:
            line_sections = line.split(' ')
            if len(line_sections[-1]) > 0:  # Check that line is not empty
                result.append(line_sections[-1])
        return result

    class StdoutCatcher:
        """
        This inner class is used to catch stdout output because the standard FTP libraries write to stdout.
        """
        def __init__(self):
            import sys
            self._txt = ''
            self._backup_stdout = sys.stdout
            sys.stdout = self

        def write(self, txt):
            self._txt += txt

        def get_text(self):
            import sys
            sys.stdout = self._backup_stdout
            return self._txt

        def __del__(self):
            import sys
            sys.stdout = self._backup_stdout  # this is done in case function get_text was not called.

    def setup_sd_card_logging(
            self,
            filename,
            start_address1=3000,
            num_of_registers1=8,
            start_address2=5000,
            num_of_registers2=0,
            start_address3=7000,
            num_of_registers3=0,
            start_address4=9000,
            num_of_registers4=0,
            interval_ms=100,
            number_of_samples=100,
    ):
        if not self._com.read_card_available():
            raise AttributeError("No SD card is inserted in COM module.")
        result = self._com.write_log_file_name(filename)
        if not result:
            raise AttributeError("filename should be 11 characters or less.")
        self._com.write_log_start_address_1(start_address1)
        self._com.write_number_of_registers_to_log_1(num_of_registers1)
        self._com.write_log_start_address_2(start_address2)
        self._com.write_number_of_registers_to_log_2(num_of_registers2)
        self._com.write_log_start_address_3(start_address3)
        self._com.write_number_of_registers_to_log_3(num_of_registers3)
        self._com.write_log_start_address_4(start_address4)
        self._com.write_number_of_registers_to_log_4(num_of_registers4)
        self._com.write_log_interval(interval_ms)
        self._com.write_log_number_of_samples(number_of_samples)
        self._com.write_log_enable(1)
        return interval_ms*number_of_samples/1000  # return how long this will take in seconds

    # Magic Methods Override.

    def __str__(self):
        return self.get_system_information()

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, item):
        return self._module_list[item]

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        try:
            a_module = self.__getitem__(self._iter_index)
            self._iter_index += 1
            return a_module
        except IndexError:
            raise StopIteration

    def __len__(self):
        return len(self._module_list)
