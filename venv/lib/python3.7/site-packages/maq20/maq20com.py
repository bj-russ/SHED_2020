from maq20.maq20module import *
from maq20.utilities import *
MODBUS_BACKEND = 0
PYMODBUS3 = 1
UMODBUS = 2

try:
    # raise ImportError("Us")
    from pymodbus3.client.sync import ModbusTcpClient
    MODBUS_BACKEND = PYMODBUS3
except ImportError:
    try:
        import socket
        from umodbus import conf
        from umodbus.client import tcp
        MODBUS_BACKEND = UMODBUS
    except:
        raise ImportError("No Modbus backend available.")


def get_modbus_backend():
    return MODBUS_BACKEND


class COMx(MAQ20Module):
    """
    COM Module:
    Takes care of the communication backend and provides functions that read the COMx register map.
    """

    def __init__(self, ip_address, port):
        if ip_address is not None or port is not None:
            if MODBUS_BACKEND == PYMODBUS3:
                self._client = ModbusTcpClient(ip_address, port=port)
            if MODBUS_BACKEND == UMODBUS:
                self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self._sock.settimeout(2)  # seconds
                self._sock.connect((ip_address, port))
        super(COMx, self).__init__(com=self, registration_number=0)

    def read_register(self, address):
        """
        Low level register access.
        Performs a modbus read register request to the MAQ20
        :param address: requested address
        :return: int - [-32767, 32767]
        """
        return self.read_registers(address, 1)[0]

    def read_registers(self, address, number_of_registers):
        """
        Low level register access.
        Performs a modbus read registers request to the MAQ20
        :param address: starting address.
        :param number_of_registers: number of registers to be read in sequence.
        :return: list(int) [-32767, 32767]
        """
        if MODBUS_BACKEND == PYMODBUS3:
            result = self._client.read_holding_registers(address=address, count=number_of_registers)
            # converts the returned values to signed.
            try:
                return [unsigned16_to_signed16(value) for value in result.registers]
            except AttributeError:
                return None
        if MODBUS_BACKEND == UMODBUS:
            message = tcp.read_holding_registers(0, address, number_of_registers)
            result = tcp.send_message(message, self._sock)
            return [unsigned16_to_signed16(value) for value in result]

    def write_register(self, address, value):
        """
        Low level register access.
        Performs a modbus write register request to the MAQ20
        :param address: starting address.
        :param value: int [-32767, 32767] or a str of size 1
        :return: modbus response.
        """
        if type(value) is str:
            value = ord(value[0])
        value = signed16_to_unsigned16(value)
        if MODBUS_BACKEND == PYMODBUS3:
            return self._client.write_register(address, value)
        if MODBUS_BACKEND == UMODBUS:
            message = tcp.write_single_register(slave_id=0,
                                                address=address,
                                                value=value)
            return tcp.send_message(message, self._sock)

    def write_registers(self, address, values=None):
        """
        Low level register access.
        Performs a modbus write registers request to the MAQ20
        :param address: starting address.
        :param values: list(int) [-32767, 32767] or a str
        :return: modbus response.
        """
        ints = []
        if type(values) is str:
            for c in values:
                ints.append(ord(c))
        else:
            ints = [signed16_to_unsigned16(x) for x in values]
        if MODBUS_BACKEND == PYMODBUS3:
            return self._client.write_registers(address, ints)
        if MODBUS_BACKEND == UMODBUS:
            message = tcp.write_multiple_registers(slave_id=0,
                                                   starting_address=address,
                                                   values=ints)
            return tcp.send_message(message, self._sock)

    def read_ip_address(self):
        return self._com.read_registers(50, 4)

    def write_ip_address(self, ip_address):
        if type(ip_address) is str:
            first = ip_address.partition('.')
            second = first[2].partition('.')
            third = second[2].partition('.')
            numbers = [first[0], second[0], third[0], third[2]]
            numbers = [int(number) for number in numbers]
            return self.write_registers(50, numbers)
        elif type(ip_address) is list:
            return self.write_registers(50, ip_address)
        return None

    def read_ethernet_subnet_mask(self):
        return self._com.read_registers(55, 4)

    def write_ethernet_subnet_mask(self, mask):
        if type(mask) is str:
            first = mask.partition('.')
            second = first[2].partition('.')
            third = second[2].partition('.')
            numbers = [first[0], second[0], third[0], third[2]]
            numbers = [int(number) for number in numbers]
            return self.write_registers(55, numbers)
        elif type(mask) is list:
            return self.write_registers(55, mask)
        return None

    def read_serial_port_baud(self) -> int:
        return{0: 1200, 1: 2400, 2: 4800, 3: 9600, 4: 19200, 5: 38400, 6: 57600, 7: 115200, 8: 230400, 9: 460800,
               10: 921600}[self._com.read_register(60)]

    def write_serial_port_baud(self, baud):
        if baud > 10:
            baud = {1200: 0, 2400: 1, 4800: 2, 9600: 3, 19200: 4, 38400: 5, 57600: 6, 115200: 7, 230400: 8,
                    460800: 9, 921600: 10}[baud]
        return self.write_register(60, baud)

    def read_serial_port_parity(self) -> str:
        return{
            0: 'None',
            1: 'Odd',
            2: 'Even'
        }[self._com.read_register(65)]

    def write_serial_port_parity(self, parity):
        if type(parity) is str:
            parity = parity.lower()
            parity = {'none': 0, 'odd': 1, 'even': 2}[parity]
        self.write_register(65, parity)

    def read_rs485_type(self):
        return {0: '4-wire', 1: '2-wire'}[self.read_register(66)]

    def write_rs485_type(self, rs485_type):
        if type(rs485_type) is str:
            if rs485_type[0] == '4':
                rs485_type = 0
            elif rs485_type[1] == '2':
                rs485_type = 1
            else:
                return None
        return self.write_register(66, rs485_type)

    def read_termination(self):
        return {0: False, 1: True}[self.read_register(67)]

    def write_termination(self, termination):
        if type(termination) is str:
            if termination[0] == 'D' or termination[0] == 'd':
                termination = 0
            elif termination[0] == 'E' or termination[0] == 'e':
                termination = 1
            else:
                return None
        if type(termination) is bool:
            termination = {False: 0, True: 1}[termination]
        return self.write_register(67, termination)

    def read_slave_id(self):
        return self.read_register(68)

    def write_slave_id(self, slave_id):
        return self.write_register(68, slave_id)

    def write_save_port_and_server_settings(self):
        """Saves the com port and file server information into the COM's EEPROM memory.
        Note: Changes apply after power cycle."""
        return self.write_register(70, 1)

    def read_file_server_username(self) -> str:
        return response_to_string(self.read_registers(71, 10))

    def write_file_server_username(self, username):
        if type(username) is not str:
            return False
        else:
            return self.write_registers(71, username)

    def read_file_server_password(self):
        return response_to_string(self.read_registers(81, 10))

    def write_file_server_password(self, password):
        if type(password) is not str:
            return False
        else:
            return self.write_registers(81, password)

    def read_file_server_anonymous_login(self):
        return self.read_register(91)

    def write_file_server_anonymous_login(self, input_value):
        return self.write_register(91, input_value)

    #######################
    # Module Configuration.
    #######################

    def read_module_status(self):
        return self.read_registers(100, 24)

    def write_module_status(self, input_value):
        # TODO: Write this function.
        pass

    def read_ethernet_port_present(self):
        return self.read_register(130)

    def read_usb_port_present(self):
        return self.read_register(131)

    def read_rs485_port_present(self):
        return self.read_register(132)

    def read_rs232_port_present(self):
        return self.read_register(133)

    def read_can_port_present(self):
        return self.read_register(134)

    ###############################
    # Registration and Data Logger.
    ###############################

    # TODO: Decide how to handle manual registration.

    def auto_registration(self, enable):
        """
        Enables or disables auto registration.
        :param enable: Boolean
        :return: response from modbus backend.
        """
        result = None
        if enable is True:
            result = self.write_register(1020, 1)  # enable auto registration
        elif enable is False:
            result = self.write_register(1020, 0)  # disable auto registration
            # """This for loop """
            # for i in range(24):
            #     self.write_register(1022, i+1)
        return result

    def delete_registration_numbers(self, numbers):
        if numbers == "all":
            for i in range(24):
                self.write_register(1022, i+1)
        try:
            for number in numbers:
                self.write_register(1022, number)
        except TypeError:
            self.write_register(1022, number)
        return True

    def register_module(self, serial_number, registration_number):
        pass

    # SD CARD

    def read_log_file_name(self):
        return utils.response_to_string(self.read_registers(1100, 11))

    def write_log_file_name(self, name: str):
        return self.write_registers(1100, name) if len(name) < 12 else False

    def read_log_start_address_1(self):
        """
        Default = 2000 (Start Address of I/O Module in Slot 1.  Data for this module is at Start Address 3000)
        :return: int
        """
        return self.read_register(1120)

    def write_log_start_address_1(self, value):
        """
        Default = 2000 (Start Address of I/O Module in Slot 1.  Data for this module is at Start Address 3000)
        :return: modbus response.
        """
        return self.write_register(1120, value)

    def read_number_of_registers_to_log_1(self):
        """
        Number of Registers to Log starting at Log Start Address 1.  Maximum = 100, Default = 8
        :return: int
        """
        return self.read_register(1121)

    def write_number_of_registers_to_log_1(self, value):
        """
        Number of Registers to Log starting at Log Start Address 1.  Maximum = 100, Default = 8
        :param value: number to write
        :return: modbus response
        """
        return self.write_register(1121, value)

    def read_log_start_address_2(self):
        """
        Default = 4000 (Start Address of I/O Module in Slot 2.  Data for this module is at Start Address 5000)
        :return: int
        """
        return self.read_register(1122)

    def write_log_start_address_2(self, value):
        """
        Default = 4000 (Start Address of I/O Module in Slot 2.  Data for this module is at Start Address 5000)
        :return: modbus response.
        """
        return self.write_register(1122, value)

    def read_number_of_registers_to_log_2(self):
        """
        Number of Registers to Log starting at Log Start Address 2.  Maximum = 100, Default = 8
        :return: int
        """
        return self.read_register(1123)

    def write_number_of_registers_to_log_2(self, value):
        """
        Number of Registers to Log starting at Log Start Address 2.  Maximum = 100, Default = 8
        :param value: number to write
        :return: modbus response
        """
        return self.write_register(1123, value)

    def read_log_start_address_3(self):
        """
        Default = 6000 (Start Address of I/O Module in Slot 3.  Data for this module is at Start Address 7000)
        :return: int
        """
        return self.read_register(1124)

    def write_log_start_address_3(self, value):
        """
        Default = 6000 (Start Address of I/O Module in Slot 3.  Data for this module is at Start Address 7000)
        :return: modbus response.
        """
        return self.write_register(1124, value)

    def read_number_of_registers_to_log_3(self):
        """
        Number of Registers to Log starting at Log Start Address 3.  Maximum = 100, Default = 8
        :return: int
        """
        return self.read_register(1125)

    def write_number_of_registers_to_log_3(self, value):
        """
        Number of Registers to Log starting at Log Start Address 3.  Maximum = 100, Default = 8
        :param value: number to write
        :return: modbus response
        """
        return self.write_register(1125, value)

    def read_log_start_address_4(self):
        """
        Default = 8000 (Start Address of I/O Module in Slot 4.  Data for this module is at Start Address 9000)
        :return: int
        """
        return self.read_register(1126)

    def write_log_start_address_4(self, value):
        """
        Default = 8000 (Start Address of I/O Module in Slot 4.  Data for this module is at Start Address 9000)
        :return: modbus response.
        """
        return self.write_register(1126, value)

    def read_number_of_registers_to_log_4(self):
        """
        Number of Registers to Log starting at Log Start Address 4.  Maximum = 100, Default = 8
        :return: int
        """
        return self.read_register(1127)

    def write_number_of_registers_to_log_4(self, value):
        """
        Number of Registers to Log starting at Log Start Address 4.  Maximum = 100, Default = 8
        :param value: number to write
        :return: modbus response
        """
        return self.write_register(1127, value)

    def read_log_interval(self):
        return utils.int16_to_int32(self.read_registers(1130, 2))

    def write_log_interval(self, value):
        return self.write_registers(1130, utils.int32_to_int16s(value))

    def read_log_number_of_samples(self):
        return utils.int16_to_int32(self.read_registers(1132, 2))

    def write_log_number_of_samples(self, value):
        return self.write_registers(1132, utils.int32_to_int16s(value))

    def read_log_enable(self):
        return self.read_register(1140)

    def write_log_enable(self, enable):
        return self.write_register(1140, enable)

    def read_card_available(self):
        return self.read_register(1150)

    def read_total_space(self):
        return utils.int16_to_int32(self.read_registers(1151, 2))

    def read_free_space(self):
        return utils.int16_to_int32(self.read_registers(1153, 2))

    #############################
    # Module RTC and Temperature.
    #############################

    def read_second(self):
        """0-59"""
        return self.read_register(1200)

    def write_second(self, second):
        """0-59"""
        return self.write_register(1200, second)

    def read_minute(self):
        """0-59"""
        return self.read_register(1201)

    def write_minute(self, minute):
        """0-59"""
        return self.write_register(1201, minute)

    def read_hour(self):
        """0-23"""
        return self.read_register(1202)

    def write_hour(self, hour):
        """0-23"""
        return self.write_register(1202, hour)

    def read_day(self):
        """1-7, 1 = Sunday"""
        return self.read_register(1203)

    def write_day(self, day):
        """1-7, 1 = Sunday"""
        return self.write_register(1203, day)

    def read_date(self):
        """1-31"""
        return self.read_register(1204)

    def write_date(self, date):
        """1-31"""
        return self.write_register(1204, date)

    def read_month(self):
        """1-12"""
        return self.read_register(1205)

    def write_month(self, month):
        """1-12"""
        return self.write_register(1205, month)

    def read_year(self):
        """0-99"""
        return self.read_register(1206)

    def write_year(self, year):
        """0-99"""
        return self.write_register(1206, year)

    def read_internal_temperature_sensor(self):
        """0-59, Degree C"""
        return self.read_register(1210)

    ######################
    # PID Loop Controllers
    ######################
    # TODO: Implement the write functions for PID loop controllers.
    # TODO: Document write functions.

    def read_pid_id(self):
        """
        Unique instance ID of Controller
        :return: 0 to 31
        """
        return self.read_register(1300)

    def write_pid_id(self, input_id):
        """
        Unique instance ID of Controller
        :return: modbus response
        """
        return self.write_register(1300, input_id) if 0 <= input_id <= 31 else False

    def read_pid_enable(self):
        """
        Enable/Disable Controller
        :return: 0 or 1
        """
        return self.read_register(1301)

    def write_pid_enable(self, enable):
        """
        Enable/Disable Controller
        :return: modbus response
        """
        return self.write_register(1301, enable)

    def read_pid_name(self):
        """
        PID Controller name, 10 characters max.
        :return: string of length 10
        """
        return response_to_string(self.read_registers(1310, 10))

    def write_pid_name(self, name):
        """
        PID Controller name, 10 characters max.
        :return: modbus response
        """
        return self.write_registers(1310, name)

    def read_pid_description(self):
        """
        PID Controller Description, 10 characters max.
        :return: string of length 10
        """
        return response_to_string(self.read_registers(1330, 10))

    def write_pid_description(self, description):
        """
        PID Controller Description, 10 characters max.
        :return: string of length 10
        """
        return self.write_registers(1330, description)

    def read_pid_engineering_units(self):
        """
        Engineering Units (EU) chosen for the Controller, 5 characters max.
        :return: string of length 5
        """
        return response_to_string(self.read_registers(1350, 5))

    def write_pid_engineering_units(self, engineering_units):
        """
        Engineering Units (EU) chosen for the Controller, 5 characters max.
        :return: string of length 5
        """
        return self.write_registers(1350, engineering_units)

    def read_pid_pv_range_unit(self):
        """
        Units chosen for Process Variable.  5 characters max.  Standard unit = "%".
        :return: string of length 5
        """
        return response_to_string(self.read_registers(1355, 5))

    def write_pid_pv_range_unit(self, pv_range_unit):
        """
        Units chosen for Process Variable.  5 characters max.  Standard unit = "%".
        :return: string of length 5
        """
        return self.write_registers(1355, pv_range_unit)

    def read_pid_co_range_unit(self):
        """
        Units chosen for Control Output.  5 characters max.  Standard unit = "%".
        :return: string of length 5
        """
        return response_to_string(self.read_registers(1360, 5))

    def write_pid_co_range_unit(self, co_range_unit):
        """
        Units chosen for Control Output.  5 characters max.  Standard unit = "%".
        :return: string of length 5
        """
        return self.write_registers(1360, co_range_unit)

    def read_pid_pv_modbus_address(self):
        """
        System Address where Process Variable is obtained from.
        :return: 0 to 65,535
        """
        return self.read_register(1366)

    def read_pid_co_modbus_address(self):
        """
        System Address where Control Output is sent to.
        :return: 0 to 65,535
        """
        return self.read_register(1367)

    def read_pid_pv_count_maximum(self):
        """
        Process Variable maximum count value.  MSB at Address 1368, LSB at Address 1369.
        :return: 0 to 2^32-1
        """
        return int16_to_int32(self.read_registers(1368, 2))

    def write_pid_pv_count_maximum(self, pv_count_maximum):
        """
        Process Variable maximum count value.  MSB at Address 1368, LSB at Address 1369.
        :return: 0 to 2^32-1
        """
        return self.write_registers(1368, int32_to_int16s(pv_count_maximum))

    def read_pid_pv_count_minimum(self):
        """
        Process Variable minimum count value.  MSB at Address 1370, LSB at Address 1371.
        :return: 0 to 2^32-1
        """
        return int16_to_int32(self.read_registers(1370, 2))

    def write_pid_pv_count_minimum(self, pv_count_minimum):
        """
        Process Variable minimum count value.  MSB at Address 1370, LSB at Address 1371.
        :return: 0 to 2^32-1
        """
        return self.write_registers(1370, int32_to_int16s(pv_count_minimum))

    def read_pid_co_count_maximum(self):
        """
        Control Output maximum count value.  MSB at Address 1372, LSB at Address 1373.
        :return: 0 to 2^32-1
        """
        return int16_to_int32(self.read_registers(1372, 2))

    def write_pid_co_count_maximum(self, co_count_maximum):
        """
        Control Output maximum count value.  MSB at Address 1372, LSB at Address 1373.
        :return: 0 to 2^32-1
        """
        return self.write_registers(1372, int32_to_int16s(co_count_maximum))

    def read_pid_co_count_minimum(self):
        """
        Control Output minimum count value.  MSB at Address 1374, LSB at Address 1375.
        :return: 0 to 2^32-1
        """
        return int16_to_int32(self.read_registers(1374, 2))

    def write_pid_co_count_minimum(self, co_count_minimum):
        """
        Control Output minimum count value.  MSB at Address 1374, LSB at Address 1375.
        :return: 0 to 2^32-1
        """
        return self.write_registers(1374, int32_to_int16s(co_count_minimum))

    def read_pid_pv_range_maximum(self):
        """
        Process Variable Range maximum value.  Integer part at Address 1376, fractional part at Address 1377.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1376, 2))

    def write_pid_pv_range_maximum(self, pv_range_maximum):
        """
        Process Variable Range maximum value.  Integer part at Address 1376, fractional part at Address 1377.
        :return: float type number
        """
        return self.write_registers(1376, float_to_ints(pv_range_maximum))

    def read_pid_pv_range_minimum(self):
        """
        Process Variable Range minimum value.  Integer part at Address 1378, fractional part at Address 1379.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1378, 2))

    def write_pid_pv_range_minimum(self, pv_range_minimum):
        """
        Process Variable Range minimum value.  Integer part at Address 1378, fractional part at Address 1379.
        :return: float type number
        """
        return self.write_registers(1378, float_to_ints(pv_range_minimum))

    def read_pid_co_range_maximum(self):
        """
        Control Output Range maximum value.  Integer part at Address 1380, fractional part at Address 1381.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1380, 2))

    def write_pid_co_range_maximum(self, co_range_maximum):
        """
        Control Output Range maximum value.  Integer part at Address 1380, fractional part at Address 1381.
        :return: float type number
        """
        return self.write_registers(1380, float_to_ints(co_range_maximum))

    def read_pid_co_range_minimum(self):
        """
        Control Output Range minimum value.  Integer part at Address 1382, fractional part at Address 1383.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1382, 2))

    def write_pid_co_range_minimum(self, co_range_minimum):
        """
        Control Output Range minimum value.  Integer part at Address 1382, fractional part at Address 1383.
        :return: float type number
        """
        return self.write_registers(1382, float_to_ints(co_range_minimum))

    def read_pid_algorithm(self):
        """
        PID Control Algorithm.  0 = Noninteractive, 1 = Parallel
        :return: string
        """
        return {0: "Noninteractive", 1: "Parallel"}[self.read_register(1386)]

    def write_pid_algorithm(self, algorithm):
        """
        PID Control Algorithm.  0 = Noninteractive, 1 = Parallel
        :return: string
        """
        return self.read_register(1386)  # TODO: Finish this.

    def read_pid_control_direction(self):
        """
        Control Direction.  0 = Reverse Acting, 1 = Direct Acting
        :return: string
        """
        return {0: "Reverse Acting", 1: "Direct Acting"}[self.read_register(1387)]

    def read_pid_setpoint_action(self):
        """
        Setpoint Action.  0 = Proportional & Derivative on Error, 1 = Proportional on Error / Derivative on PV,
        2 = Proportional & Derivative on PV.
        :return: string
        """
        return {0: "Proportional & Derivative on Error",
                1: "Proportional on Error / Derivative on PV",
                2: "Proportional & Derivative on PV",
                }[self.read_register(1388)]

    def write_pid_setpoint_action(self, setpoint_action):
        """
        Setpoint Action.  0 = Proportional & Derivative on Error, 1 = Proportional on Error / Derivative on PV,
        2 = Proportional & Derivative on PV.
        :return: string
        """
        return self.read_register(1388)

    def read_pid_mode(self):
        """
        Operational Mode.  0 = Manual, 1 = Automatic
        :return: string
        """
        return {0: "Manual", 1: "Automatic"}[self.read_register(1389)]

    def read_pid_output_type(self):
        """
        Control Output Signal Type.  0 = Voltage, 1 = Current, 2 = Discrete Output (PWM)
        :return: string
        """
        return {0: "Voltage", 1: "Current", 2: "Discrete Output (PWM)"}[self.read_register(1390)]

    def read_pid_setpoint(self):
        """
        Setpoint.
        Integer part at Address 1396, fractional part at Address 1397.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1396, 2))

    def read_pid_process_variable(self):
        """
        Process Variable.
        Integer part at Address 1398, fractional part at Address 1399.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1398, 2))

    def read_pid_control_output(self):
        """
        Control Output.
        Integer part at Address 1400, fractional part at Address 1401.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1400, 2))

    def read_pid_pv_maximum(self):
        """
        Process Variable maximum value.
        Integer part at Address 1402, fractional part at Address 1403.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1402, 2))

    def read_pid_pv_minimum(self):
        """
        Process Variable minimum value.
        Integer part at Address 1404, fractional part at Address 1405.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1404, 2))

    def read_pid_co_maximum(self):
        """
        Control Output maximum value.
        Integer part at Address 1406, fractional part at Address 1407.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1406, 2))

    def read_pid_co_minimum(self):
        """
        Control Output minimum value.
        Integer part at Address 1408, fractional part at Address 1409.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1408, 2))

    def read_pid_kc(self):
        """
        Controller Gain (%/%).
        Integer part at Address 1410, fractional part at Address 1411.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1410, 2))

    def read_pid_ti(self):
        """
        Integral Time (minutes).
        Integer part at Address 1412, fractional part at Address 1413.  Fractional part is in 10,000ths of a second.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1412, 2))

    def read_pid_td(self):
        """
        Derivative Time (minutes).
        Integer part at Address 1414, fractional part at Address 1415.  Fractional part is in 10,000ths of a second.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1414, 2))

    def read_pid_scan_time(self):
        """
        PID Controller Update Rate (seconds).
        Integer part at Address 1416, fractional part at Address 1417.  This value is fixed at 1s.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1416, 2))

    def read_pid_co_high_clamp(self):
        """
        Controller Output upper limit (%).
        Integer part at Address 1418, fractional part at Address 1419.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1418, 2))

    def read_pid_co_low_clamp(self):
        """
        Controller Output lower limit (%).
        Integer part at Address 1420, fractional part at Address 1421.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1420, 2))

    def read_pid_pv_tracking(self):
        """
        Track Process Variable in Manual Mode. 0 = Do Not Track PV, 1 = Track PV
        :return: string
        """
        return {0: "Do Not Track PV", 1: "Track PV"}[self.read_register(1422)]

    def read_pid_gap_width(self):
        """
        Gap around setpoint (Engineering Units).
        Integer part at Address 1423, fractional part at Address 1424.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1423, 2))

    def read_pid_gap_multiplier(self):
        """
        Gain multiplier inside Gap.
        Integer part at Address 1425, fractional part at Address 1426.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1425, 2))

    def read_pid_filter_time_constant(self):
        """
        PV Filter Time Constant (minutes).
        Integer part at Address 1427, fractional part at Address 1428. Fractional part is in 10,000ths of a second.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1427, 2))

    def read_pid_active_alarm(self):
        """
        Indicates which alarm condition is active. 0 = Low-Low, 1 = Low, 2 = None, 3 = High-High, 4 = High.
        :return: string
        """
        return {0: "Low-Low",
                1: "Low",
                2: "None",
                3: "High-High",
                4: "High",
                }[self.read_register(1441)]

    def read_pid_alarm_deadband(self):
        """
        Deadband or Hysteresis.  Adds to low limits, subtracts from high limits.
        Integer part at Address 1442, fractional part at Address 1443.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1442, 2))

    def read_pid_high_high_alarm_limit(self):
        """
        High-High Alarm Limit (Engineering Units). Integer part at Address 1444, fractional part at Address 1445.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1444, 2))

    def read_pid_high_alarm_limit(self):
        """
        High Alarm Limit (Engineering Units). Integer part at Address 1446, fractional part at Address 1447.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1446, 2))

    def read_pid_low_alarm_limit(self):
        """
        Low Alarm Limit (Engineering Units). Integer part at Address 1448, fractional part at Address 1449.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1448, 2))

    def read_pid_low_low_alarm_limit(self):
        """
        Low-Low Alarm Limit (Engineering Units). Integer part at Address 1450, fractional part at Address 1451.
        :return: float type number
        """
        return ints_to_float(self.read_registers(1450, 2))

    ###################
    # Helper Functions.
    ###################

    def ftp_settings(self) -> str:
        # TODO: Document this function.
        result = "Username: "
        username = self.read_registers(71, 10)
        result += response_to_string(username) + "\n"
        result += "Password: "
        password = self.read_registers(81, 10)
        result += response_to_string(password) + "\n"
        result += "Anonymous Login: "
        anonymous_login = self.read_register(91)
        if anonymous_login == 1:
            result += "Enabled"
        elif anonymous_login == 0:
            result += "Disabled"
        return result

    def __del__(self):
        if MODBUS_BACKEND == PYMODBUS3:
            self._client.close()
        if MODBUS_BACKEND == UMODBUS:
            self._sock.close()
        # print("\n\n-------------------------------------------------------------------------")
        # print("MAQ20 connection closed.")
