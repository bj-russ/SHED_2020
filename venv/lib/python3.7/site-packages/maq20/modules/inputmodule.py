from maq20.maq20module import MAQ20Module
import maq20.utilities as utils


class InputModule(MAQ20Module):

    def __init__(self, maq20_module):
        if isinstance(maq20_module, MAQ20Module):
            super(InputModule, self).__init__(com=maq20_module.get_com_module(),
                                              registration_number=maq20_module.get_registration_number())
        else:
            raise RuntimeError('Passed in object is not MAQ20 object.')

    ###############
    # Data minimum.
    ###############

    # Counts:

    def read_channel_data_minimum_counts(self, channel):
        return self._read_channel_data_counts_address_input(1030, channel)

    def read_data_minimum_counts(self, start_channel=0, number_of_channels=1):
        return self._read_data_counts_address_input(1030, start_channel, number_of_channels)

    # Engineering values:

    def read_channel_data_minimum(self, channel):
        return self._read_channel_data_address_input(1030, channel)

    def read_data_minimum(self, start_channel=0, number_of_channels=1):
        return self._read_data_address_input(1030, start_channel, number_of_channels)

    # Reset:

    def write_channel_data_minimum_reset(self, channel):
        """
        This will reset the data minimum tracker in the module.
        :return: modbus response
        """
        return self.write_register(1030 + channel, 0)

    ###############
    # Data maximum.
    ###############

    # Counts:

    def read_channel_data_maximum_counts(self, channel):
        return self._read_channel_data_counts_address_input(1050, channel)

    def read_data_maximum_counts(self, start_channel=0, number_of_channels=1):
        return self._read_data_counts_address_input(1050, start_channel, number_of_channels)

    # Engineering values:

    def read_channel_data_maximum(self, channel):
        return self._read_channel_data_address_input(1050, channel)

    def read_data_maximum(self, start_channel=0, number_of_channels=1):
        return self._read_data_address_input(1050, start_channel, number_of_channels)

    # Reset:

    def write_channel_data_maximum_reset(self, channel):
        """
        This will reset the data maximum tracker in the module
        :return: modbus response
        """
        return self.write_register(1050 + channel, 0)

    ###############
    # Data average.
    ###############

    # Counts:

    def read_channel_data_average_counts(self, channel=0):
        return self._read_channel_data_counts_address_input(1070, channel)

    def read_data_average_counts(self, start_channel=0, number_of_channels=1):
        return self._read_data_counts_address_input(1070, start_channel, number_of_channels)

    # Engineering values:

    def read_channel_data_average(self, channel=0):
        return self._read_channel_data_address_input(1070, channel)

    def read_data_average(self, start_channel=0, number_of_channels=1):
        return self._read_data_address_input(1070, start_channel, number_of_channels)

    # Reset:

    def write_channel_data_average_reset(self, channel):
        """
        This will reset the data average tracker in the module
        :return: modbus response
        """
        return self.write_register(1070 + channel, 0)

    ###############
    # Data History.
    ###############

    def read_data_history_counts(self, channel):
        self._check_channel_inputs(channel)  # Check input.
        return self.read_registers(1070 + (channel * 10), 10)

    def read_data_history(self, channel):
        counts = self.read_data_history_counts(channel)
        return [utils.counts_to_engineering_units_dict_input(counts, self.get_channel_ranges_information(channel))]

    #######################
    # Module Configuration.
    #######################

    def read_input_range(self, channel=0):
        """
        Current range configuration for channel.
        :param channel: zero indexed channel number requested.
        :return:
        """
        return self.read_register(100 + channel)

    def write_input_range(self, channel=0, new_range=None):
        """
        Write a new range for channel index passed in.
        :param channel: int
        :param new_range: int
        :return: modbus response
        """
        if 0 < channel < self._number_of_channels and new_range < self._number_of_ranges:
            self._channel_active_ranges[channel] = new_range
            return self.write_register(100 + channel, new_range)
        else:
            return False

    def write_save_to_eeprom(self):
        """
        Save range, average weight, and scan list to the module's EEPROM.
        :return: modbus response.
        """
        self.write_register(119, 0)

    def read_average_weight(self, channel=0):
        """
        Signal averaging can be set on a per-channel basis by configuring the Average Weight. Average
        Weight is calculated as 2^x where x = 0 to 15 and the default value is x = 0. The running average
        is then calculated as follows:
        Average = Average + ((Sampled Value – Average) / Average Weight)
        :param channel: channel requested
        :return: int from 0 to 15
        """
        return self.read_register(120 + channel)

    def write_average_weight(self, channel=0, new_weight=None):
        """
        Signal averaging can be set on a per-channel basis by configuring the Average Weight. Average
        Weight is calculated as 2^x where x = 0 to 15 and the default value is x = 0. The running average
        is then calculated as follows:
        Average = Average + ((Sampled Value – Average) / Average Weight)
        :param channel: channel to write to.
        :param new_weight: new value from 0 to 15
        :return:
        """
        return self.write_register(120 + channel, new_weight)

    def read_channel_enable(self, channel=0):
        """
        Read the channel enable state of the channel requested.
        :param channel: channel requested
        :return:  int, 0 or 1, 0 : disabled, 1 : enabled.
        """
        return self.read_register(140 + channel)

    def write_channel_enable(self, channel=0, enable=None):
        """
        Write the channel enable state of the channel requested.
        :param channel: channel to write to.
        :param enable: 0 or 1. 0: disable, 1: enable
        :return: modbus response
        """
        return self.write_register(140 + channel, enable)
