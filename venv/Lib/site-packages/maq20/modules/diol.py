from maq20 import MAQ20Module
from maq20 import utilities as utils


class DIOL(MAQ20Module):
    """
    This class is used for both the DIOL modules and DIOH modules.
    """

    def __init__(self, maq20_module):
        """
        :param maq20_module: pass in the module returned by MAQ20.get_module_list()
        """
        if isinstance(maq20_module, MAQ20Module):
            super(DIOL, self).__init__(com=maq20_module.get_com_module(),
                                       registration_number=maq20_module.get_registration_number())
        else:
            raise RuntimeError('Passed in object is not MAQ20 object.')

    ######################
    # Module Configuration
    ######################

    def read_channel_configuration(self, channel=0):
        """
        1: Input or 2: Output
        :param channel: channel requested.
        :return: integer
        """
        return self.read_register(100+channel)

    def read_default_output_configuration(self, channel=0):
        """
        Discrete Output Default State.  Default = 1 for all channels.
        DO0 - DO3
        0 = Switch Closed
        1 = Switch Open
        :param channel: channel requested
        :return: integer
        """
        return self.read_register(110+channel)

    def write_default_output_configuration(self, channel=0, input_val=1):
        """
        Discrete Output Default State.  Default = 1 for all channels.
        DO0 - DO3
        0 = Switch Closed
        1 = Switch Open
        :param channel: channel requested
        :param input_val: integer
        :return: modbus response
        """
        return self.write_register(110+channel, input_val)

    def write_save_to_eeprom(self):
        """
        Saves the Default Output Configuration to the eeprom in the module.
        :return: modbus response
        """
        return self.write_register(190, 0)

    ###################################################
    # Data and Special Function Selection. [1000, 1299]
    ###################################################

    def read_dio_state(self, channel=0):
        return self.read_register(1000+channel)

    def read_dio_states_binary(self):
        return self.read_registers(1000, self._number_of_channels)

    def read_dio_states_decimal(self):
        return self.read_register(1010)

    def write_data_out(self, do0_do4):
        """
        Writes the passed in 'state' to the output channels of the DIO. example of input: [0,1,1,0,1]
        :param do0_do4: list(int) of size 5, numbers inside must be 0 or 1
        :return: modbus response
        """
        return self.write_registers(1000, do0_do4)

    # TODO: Document DIOL Special Functions.

    def read_special_functions_state(self, timer):
        start_address = {0: 1100, 1: 1200}[timer]
        return self.read_registers(start_address, 2)

    def write_special_function_0_none(self, timer):
        function = 0
        start_address = {0: 1100, 1: 1200}[timer]
        self.write_register(start_address + 1, 0)  # disarm previous special function to enable this one.

        # Special Function Configuration [0,12]
        self.write_registers(start_address, [
            function,  # 0
        ])

    def write_special_function_1_pulse_frequency_counter(self,
                                                         timer,
                                                         pulses_per_revolution=1,
                                                         internal_trigger=0,
                                                         external_enable=0,
                                                         ):
        """
        The Pulse Counter function uses discrete input channel DI0 if Timer 0 is used to implement the
        function or discrete input channel DI2 if Timer 1 is used to implement the function. Pulses on the
        input are cumulatively counted to an upper limit of 10,000,000. Input levels over 1.6V are detected
        as high and input levels below 1.6V are low. The MAQ20-DIOL module uses inverted logic so
        inputs over the threshold are reported as logic 0 and inputs below the threshold are reported as
        logic 1. Edge triggering can be set to positive or negative. If pulses per revolution is specified,
        RPM can be measured to an upper limit of 65,535. Counting is enabled or disabled by arming or
        disarming the function. Optionally, counting can be controlled using an external signal applied to
        discrete input channel DI1 if Timer 0 is used to implement the function or discrete input channel DI3
        if Timer 1 is used to implement the function. The external enable can be configured as either active
        low or active high. Pulse count is reset by writing a register.
        :param timer: 0 or 1
        :param pulses_per_revolution:
        :param internal_trigger:
        :param external_enable:
        :return:
        """
        function = 1
        start_address = {0: 1100, 1: 1200}[timer]
        self.write_register(start_address + 1, 0)  # disarm previous special function to enable this one.

        # Special Function Configuration [0,12]
        self.write_registers(start_address, [
            function,  # 0
            0,
            0,
            0,
            0,
            0,  # 5
            0,
            0,
            0,
            pulses_per_revolution,
            internal_trigger,  # 10
            external_enable,
            0,
        ])

        self.write_register(start_address + 1, 1)  # Enable/arm special function.

        status = self.read_register(start_address+2)

        # if not status:  # No errors.
        #     self.write_register(start_address+90, 0)  # Save settings to EEPROM.

        return status

    def read_special_function_1_pulse_frequency_counter(self, timer):
        """
        Reads module's settings and constructs a human readable string containing the settings read.
        :param timer: timer to be read, integer.
        :return: string
        """
        response = self.read_registers({0: 1100, 1: 1200}[timer], 13)
        pulse_count = utils.int16_to_int32(response[4:6])
        frequency = utils.int16_to_int32(response[6:8])
        return "Function              : 1 = Pulse/Frequency Counter\n" \
               "Arm/Disarm            : {0[1]}\n" \
               "Function Status       : {0[2]}\n" \
               "Alarm Status          : {0[3]}\n" \
               "Pulse Count           : {1}\n" \
               "Frequency             : {2}\n" \
               "RPM                   : {0[8]}\n" \
               "Pulses Per Revolution : {0[9]}\n" \
               "Internal Trigger      : {0[10]}\n" \
               "External Enable       : {0[11]}\n" \
               "External Enable Status: {0[12]}\n".format(response, pulse_count, frequency)

    def write_special_function_2_pulse_frequency_counter_with_debounce(self,
                                                                       timer,
                                                                       internal_trigger=0,
                                                                       debounce_output_enable=0,
                                                                       low_time=100,
                                                                       high_time=100,
                                                                       ):
        """
        The Pulse Counter with Debounce function uses discrete input channel DI0 if Timer 0 is used to
        implement the function or discrete input channel DI2 if Timer 1 is used to implement the function.
        Pulses on the input are cumulatively counted to an upper limit of 10,000,000. Input levels over 1.6V
        are detected as high and input levels below 1.6V are low. The MAQ20-DIOL module uses inverted
        logic so inputs over the threshold are reported as logic 0 and inputs below the threshold are
        reported as logic 1. Minimum Low Time and Minimum High Time for valid pulses are specified in
        increments of 100µs. These can be used to prevent false triggering from invalid signals. A
        debounced version of the input signal is provided on discrete output channel DO0 if Timer 0 is used
        to implement the function or discrete output channel DO2 if Timer 1 is used to implement the
        function. This output can be enabled or disabled by writing to a register. Edge triggering can be
        set to positive or negative. Counting is enabled or disabled by arming or disarming the function.
        Pulse count is reset by writing to a register.
        :param timer:
        :param internal_trigger:
        :param debounce_output_enable:
        :param low_time:
        :param high_time:
        :return:
        """
        function = 2
        start_address = {0: 1100, 1: 1200}[timer]
        self.write_register(start_address + 1, 0)  # disarm previous special function to enable this one.

        # Special Function Configuration [0,12]
        self.write_registers(start_address, [
            function,  # 0
            0,
            0,
            0,
            0,
            0,  # 5
            0,
            0,
            internal_trigger,
            debounce_output_enable,
            low_time,  # 10
            high_time,
        ])

        self.write_register(start_address + 1, 1)  # Enable/arm special function.

        status = self.read_register(start_address + 2)

        # if not status:  # No errors.
        #     self.write_register(start_address + 90, 0)  # Save settings to EEPROM.

        return status

    def read_special_function_2_pulse_frequency_counter_with_debounce(self, timer):
        """
        Reads module's settings and constructs a human readable string containing the settings read.
        :param timer: timer to be read, integer.
        :return: string
        """
        response = self.read_registers({0: 1100, 1: 1200}[timer], 12)
        pulse_count = utils.int16_to_int32(response[4:6])
        frequency = utils.int16_to_int32(response[6:8])
        return "Function              : 2 = Pulse/Frequency Counter w/ Debounce\n" \
               "Arm/Disarm            : {0[1]}\n" \
               "Function Status       : {0[2]}\n" \
               "Alarm Status          : {0[3]}\n" \
               "Pulse Count           : {1}\n" \
               "Frequency             : {2}\n" \
               "Internal Trigger      : {0[8]}\n" \
               "Debounce Output Enable: {0[9]}\n" \
               "Low Time (x 100us)    : {0[10]}\n" \
               "High Time (x 100us)   : {0[11]}\n".format(response, pulse_count, frequency)

    def write_special_function_3_waveform_measurement(self,
                                                      timer,
                                                      timebase=1,
                                                      internal_trigger=0,
                                                      events_to_measure=0,
                                                      average_weight=4,
                                                      ):
        function = 3
        start_address = {0: 1100, 1: 1200}[timer]
        self.write_register(start_address + 1, 0)  # disarm previous special function to enable this one.
        events_to_measure = utils.int32_to_int16s(events_to_measure)

        # Special Function Configuration [0,12]
        self.write_registers(start_address, [
            function,  # 0
            0,
            0,
            0,
            0,
        ])

        # Special Function Continuation.
        self.write_registers(start_address+30, [
            timebase,
            internal_trigger,
            events_to_measure[0],
            events_to_measure[1],
            average_weight,
        ])

        self.write_register(start_address + 1, 1)  # Enable/arm special function.

        status = self.read_register(start_address + 2)

        # if not status:  # No errors.
        #     self.write_register(start_address + 90, 0)  # Save settings to EEPROM.

        return status

    def read_special_function_3_waveform_measurement(self, timer):
        """
        Reads module's settings and constructs a human readable string containing the settings read.
        :param timer: timer to be read, integer.
        :return: string
        """
        response = self.read_registers({0: 1100, 1: 1200}[timer], 35)
        events_measured = utils.int16_to_int32(response[4:6])
        frequency = utils.int16_to_int32(response[6:8])
        period = utils.int16_to_int32(response[10:12])
        low_time = utils.int16_to_int32(response[12:14])
        high_time = utils.int16_to_int32(response[14:16])
        avg_low_time = utils.int16_to_int32(response[16:18])
        avg_high_time = utils.int16_to_int32(response[18:20])
        max_low_time = utils.int16_to_int32(response[20:22])
        min_low_time = utils.int16_to_int32(response[22:24])
        max_high_time = utils.int16_to_int32(response[24:26])
        min_high_time = utils.int16_to_int32(response[26:28])
        events_to_measure = utils.int16_to_int32(response[32:34])
        return "Function         : 3 = Waveform Measurement\n" \
               "Arm/Disarm       : {0[1]}\n" \
               "Function Status  : {0[2]}\n" \
               "Alarm Status     : {0[3]}\n" \
               "Events Measured  : {1}\n" \
               "Frequency        : {2}\n" \
               "Duty Cycle       : {0[8]}\n" \
               "Period           : {3}\n" \
               "Low Time         : {4}\n" \
               "High Time        : {5}\n" \
               "Avg Low Time     : {6}\n" \
               "Avg High Time    : {7}\n" \
               "Max Low Time     : {8}\n" \
               "Min Low Time     : {9}\n" \
               "Max High Time    : {10}\n" \
               "Min High Time    : {11}\n" \
               "Timebase         : {0[30]}\n" \
               "Internal Trigger : {0[31]}\n" \
               "Events To Measure: {12}\n" \
               "Average Weight   : {0[34]}\n".format(response, events_measured, frequency, period, low_time,
                                                     high_time, avg_low_time, avg_high_time, max_low_time,
                                                     min_low_time, max_high_time, min_high_time, events_to_measure)

    def write_special_function_4_time_between_events(self,
                                                     timer,
                                                     timebase=1,
                                                     event_1_internal_trigger=0,
                                                     event_2_internal_trigger=0,
                                                     average_weight=4,
                                                     events_to_measure=0,
                                                     ):
        function = 4
        start_address = {0: 1100, 1: 1200}[timer]
        self.write_register(start_address + 1, 0)  # disarm previous special function to enable this one.
        events_to_measure = utils.int32_to_int16s(events_to_measure)

        # Special Function Configuration [0,12]
        self.write_registers(start_address, [
            function,  # 0
            0,
            0,
            0,
            0,
            0,  # 5
            0,
            0,
            0,
            0,
            0,  # 10
            0,
            0,
            0,
            0,
            0,  # 15
            timebase,
            event_1_internal_trigger,
            event_2_internal_trigger,
            average_weight,
            events_to_measure[0],  # 20
            events_to_measure[1],
        ])

        self.write_register(start_address + 1, 1)  # Enable/arm special function.

        status = self.read_register(start_address + 2)

        # if not status:  # No errors.
        #     self.write_register(start_address + 90, 0)  # Save settings to EEPROM.

        return status

    def read_special_function_4_time_between_events(self, timer):
        """
        Reads module's settings and constructs a human readable string containing the settings read.
        :param timer: timer to be read, integer.
        :return: string
        """
        response = self.read_registers({0: 1100, 1: 1200}[timer], 22)
        events_measured = utils.int16_to_int32(response[4:6])
        frequency = utils.int16_to_int32(response[6:8])
        time_between_events_curr = utils.int16_to_int32(response[8:10])
        time_between_events_max = utils.int16_to_int32(response[10:12])
        time_between_events_min = utils.int16_to_int32(response[12:14])
        time_between_events_average = utils.int16_to_int32(response[14:16])
        events_to_measure = utils.int16_to_int32(response[20:22])
        return "Function                    : 4 = Time Between Events\n" \
               "Arm/Disarm                  : {0[1]}\n" \
               "Function Status             : {0[2]}\n" \
               "Alarm Status                : {0[3]}\n" \
               "Events Measured             : {1}\n" \
               "Frequency                   : {2}\n" \
               "Time Between Events, current: {3}\n" \
               "Time Between Events, max    : {4}\n" \
               "Time Between Events, min    : {5}\n" \
               "Time Between Events, average: {6}\n" \
               "Timebase                    : {0[16]}\n" \
               "Event 1 Internal Trigger    : {0[17]}\n" \
               "Event 2 Internal Trigger    : {0[18]}\n" \
               "Average Weight              : {0[19]}\n" \
               "Events to measure           : {7}\n".format(response, events_measured, frequency,
                                                            time_between_events_curr,
                                                            time_between_events_max, time_between_events_min,
                                                            time_between_events_average, events_to_measure)

    def write_special_function_5_frequency_generator(self,
                                                     timer,
                                                     frequency,
                                                     ):
        function = 5
        start_address = {0: 1100, 1: 1200}[timer]
        self.write_register(start_address + 1, 0)  # disarm previous special function to enable this one.
        frequency_16 = utils.int32_to_int16s(frequency)

        # Special Function Configuration [0,12]
        self.write_registers(start_address, [
            function,  # 0
            0,
            0,
            0,
            frequency_16[0],
            frequency_16[1],
        ])

        self.write_register(start_address + 1, 1)  # Enable/arm special function.

        status = self.read_register(start_address + 2)

        # if not status:  # No errors.
        #     self.write_register(start_address + 90, 0)  # Save settings to EEPROM.

        return status

    def read_special_function_5_frequency_generator(self, timer):
        """
        Reads module's settings and constructs a human readable string containing the settings read.
        :param timer: timer to be read, integer.
        :return: string
        """
        response = self.read_registers({0: 1100, 1: 1200}[timer], 22)
        frequency = utils.int16_to_int32(response[4:6])
        return "Function                    : 5 = Frequency Generator\n" \
               "Arm/Disarm                  : {0[1]}\n" \
               "Frequency                   : {1}\n".format(response, frequency)

    def write_special_function_6_pwm_generator(self,
                                               timer,
                                               timebase=1,
                                               output_2_enable=0,
                                               period=500,
                                               output_1_low_time=250,
                                               output_2_low_time=250,
                                               ):
        """
        The Pulse Width Modulation Generator function uses discrete output channels DO0 and DO1 if
        Timer 0 is used to implement the function or discrete output channels DO2 and DO3 if Timer 1 is
        used to implement the function. One or two output signals can be generated for each
        implementation of the function. If two signals are generated using a given Timer, both will have the
        same period, but duty cycle for each can be independently controlled. Output DO0 for Timer 0
        implementation or output DO2 for Timer 1 implementation are automatically enabled when the
        function is configured. Output DO1 for Timer 0 implementation or output DO3 for Timer 1
        implementation are enabled or disabled by writing to a register. All PWM outputs are enabled or
        disabled by arming or disarming the function. Period and each output low time are set by writing to
        a register. Minimum period is 200µs and minimum low time is 100µs. The timebase is selected as
        seconds, milliseconds or microseconds based on the waveform to be generated in order to obtain
        the best resolution and performance. The example shown in Figure 13 below shows the use of
        both Timers, each used to generate two PWM signals.
        :param timer:
        :param timebase:
        :param output_2_enable:
        :param period:
        :param output_1_low_time:
        :param output_2_low_time:
        :return:
        """
        function = 6
        start_address = {0: 1100, 1: 1200}[timer]
        self.write_register(start_address + 1, 0)  # disarm previous special function to enable this one.
        period = utils.int32_to_int16s(period)
        output_1_low_time = utils.int32_to_int16s(output_1_low_time)
        output_2_low_time = utils.int32_to_int16s(output_2_low_time)
        self.write_registers(start_address, [
            function,  # 0
            0,
            0,
            timebase,
            output_2_enable,
            0,  # 5
            period[0],
            period[1],
            output_1_low_time[0],
            output_1_low_time[1],
            output_2_low_time[0],  # 10
            output_2_low_time[1],
        ])

        self.write_register(start_address + 1, 1)  # Enable/arm special function.

        status = self.read_register(start_address + 2)

        # if not status:  # No errors.
        #     self.write_register(start_address + 90, 0)  # Save settings to EEPROM.

        return status

    def read_special_function_6_pwm_generator(self, timer):
        """
        Reads module's settings and constructs a human readable string containing the settings read.
        :param timer: timer to be read, integer.
        :return: string
        """
        response = self.read_registers({0: 1100, 1: 1200}[timer], 12)
        period = utils.int16_to_int32(response[6:8])
        output_1_low_time = utils.int16_to_int32(response[8:10])
        output_2_low_time = utils.int16_to_int32(response[10:12])
        return "Function         : 6 = PWM Generator\n" \
               "Arm/Disarm       : {0[1]}\n" \
               "Timebase         : {0[3]}\n" \
               "Output 2 Enable  : {0[4]}\n" \
               "Period           : {1}\n" \
               "Output 1 Low Time: {2}\n" \
               "Output 2 Low Time: {3}\n".format(response, period, output_1_low_time, output_2_low_time)

    def write_special_function_7_one_shot_pulse_generator(self,
                                                          timer,
                                                          timebase=1,
                                                          pulse_count_limit=0,
                                                          output_pulse_polarity=0,
                                                          trigger=0,
                                                          pulse_width=500,
                                                          pre_delay=100,
                                                          post_delay=100,
                                                          ):
        function = 7
        start_address = {0: 1100, 1: 1200}[timer]
        self.write_register(start_address + 1, 0)  # disarm previous special function to enable this one.
        pulse_count_limit = utils.int32_to_int16s(pulse_count_limit)
        pulse_width = utils.int32_to_int16s(pulse_width)
        pre_delay = utils.int32_to_int16s(pre_delay)
        post_delay = utils.int32_to_int16s(post_delay)
        self.write_registers(start_address, [
            function,  # 0
            0,
            0,
            timebase,
            0,
            0,  # 5
            pulse_count_limit[0],
            pulse_count_limit[1],
            output_pulse_polarity,
            trigger,
            pulse_width[0],  # 10
            pulse_width[1],
            pre_delay[0],
            pre_delay[1],
            post_delay[0],
            post_delay[1],  # 15
        ])

        self.write_register(start_address + 1, 1)  # Enable/arm special function.

        status = self.read_register(start_address + 2)

        # if not status:  # No errors.
        #     self.write_register(start_address + 90, 0)  # Save settings to EEPROM.

        return status

    def read_special_function_7_one_shot_pulse_generator(self, timer):
        """
        Reads module's settings and constructs a human readable string containing the settings read.
        :param timer: timer to be read, integer.
        :return: string
        """
        response = self.read_registers({0: 1100, 1: 1200}[timer], 16)
        pulse_count = utils.int16_to_int32(response[4:6])
        pulse_count_limit = utils.int16_to_int32(response[6:8])
        pulse_width = utils.int16_to_int32(response[10:12])
        pre_delay = utils.int16_to_int32(response[12:14])
        post_delay = utils.int16_to_int32(response[14:16])
        return "Function             : 7 = One-Shot Pulse Generator\n" \
               "Arm/Disarm           : {0[1]}\n" \
               "Timebase             : {0[3]}\n" \
               "Pulse Count          : {1}\n" \
               "Pulse Count Limit    : {2}\n" \
               "Output Pulse Polarity: {0[8]}\n" \
               "Trigger              : {0[9]}\n" \
               "Pulse Width          : {3}\n" \
               "Pre-delay            : {4}\n" \
               "Post-delay           : {5}\n".format(response, pulse_count, pulse_count_limit, pulse_width,
                                                     pre_delay, post_delay)

    def write_special_function_7_software_trigger(self, timer):
        start_address = {0: 1100, 1: 1200}[timer]
        return self.write_register(start_address+20, 0)

    def read_special_function_information(self, timer):
        start_address = {0: 1100, 1: 1200}[timer]
        current_function = self.read_register(start_address)
        if current_function == 1:
            result = self.read_special_function_1_pulse_frequency_counter(timer)
        elif current_function == 2:
            result = self.read_special_function_2_pulse_frequency_counter_with_debounce(timer)
        elif current_function == 3:
            result = self.read_special_function_3_waveform_measurement(timer)
        elif current_function == 4:
            result = self.read_special_function_4_time_between_events(timer)
        elif current_function == 5:
            result = self.read_special_function_5_frequency_generator(timer)
        elif current_function == 6:
            result = self.read_special_function_6_pwm_generator(timer)
        elif current_function == 7:
            result = self.read_special_function_7_one_shot_pulse_generator(timer)
        else:
            result = "No special function selected."
        return result


if __name__ == '__main__':
    from maq20 import MAQ20

    maq20 = MAQ20()
    diol = maq20.find("DIOL")

    diol = DIOL(diol)

    print(diol.read_special_function_information(0))
    print(diol.read_special_function_information(1))

    # diol.write_special_function_0_none(0)
    # diol.write_special_function_1_pulse_frequency_counter(0)
    # diol.write_special_function_2_pulse_frequency_counter_with_debounce(0)
    # diol.write_special_function_3_waveform_measurement(0)
    # diol.write_special_function_4_time_between_events(0)
    # diol.write_special_function_5_frequency_generator(0, 2)
    # diol.write_special_function_6_pwm_generator(0)
    # diol.write_special_function_7_one_shot_pulse_generator(0, pulse_count_limit=10, output_pulse_polarity=1)
    # diol.write_special_function_7_software_trigger(0)

    print(diol.read_special_function_information(0))
    print(diol.read_special_function_information(1))
