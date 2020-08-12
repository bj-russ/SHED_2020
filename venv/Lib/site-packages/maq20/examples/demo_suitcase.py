"""
This example was written to work with Dataforth's Demo suitcase's Process Simulator.
The Hardware is not needed to run this example.
This example uses PyQT5 and was designed using QT Designer.
'demo_suitcase_ui.py' is the output of the make_ui() function, this file is not meant to be modified directly.
"""
from maq20 import MAQ20, MAQ20Module
from maq20.modules import diol
from PyQt5.QtCore import QTimer, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from maq20.examples.demo_suitcase_ui import Ui_MainWindow
import time


def make_ui():
    """
    This function only needs to be called when modifying the designer file demo_box.ui
    Converts the ui into callable python code then saved in the file demo_box_ui.py
    """
    from PyQt5 import uic
    with open("demo_suitcase_ui.py", 'w') as file:
        res = uic.compileUi("demo_suitcase.ui", execute=True, pyfile=file)
    return res


class DemoBox(QMainWindow, Ui_MainWindow):

    def __init__(self):
        """
        - Sets up the UI built using QT Designer.
        - Connects the signals to the slots in this example.
        - Slot functions are decorated with @pyqtSlot(), this lets a programmer know that that function is meant to be a
          slot for PyQT.
        - Tries to connect to a MAQ20 system automatically, but does not crash if it can't.
        """
        super(DemoBox, self).__init__()
        self.setupUi(self)
        self.actionConnect.triggered.connect(self.init_maq20)
        self.actionAbout.triggered.connect(self.copyright)
        self.connect_button.clicked.connect(self.init_maq20)
        self.freq_slider.valueChanged['int'].connect(self.freq_slider_val)
        self.vout1_slider.valueChanged['int'].connect(self.vout1_slider_val)
        self.vout2_slider.valueChanged['int'].connect(self.vout2_slider_val)
        self.vout3_slider.valueChanged['int'].connect(self.vout3_slider_val)
        self.led_bar_control_checkbox.toggled['bool'].connect(self.led_control)
        self.motor_pot_1.valueChanged['int'].connect(self.motor_pot_1_val)
        self.motor_pot_2.valueChanged['int'].connect(self.motor_pot_2_val)
        self.tc_heat_1_spinbox.valueChanged['double'].connect(self.internal_tc_heat_1)
        self.tc_heat_2_spinbox.valueChanged['double'].connect(self.internal_tc_heat_2)

        # Setting the window logo.
        try:
            self.setWindowIcon(QIcon('logo.png'))
        except Exception as e:
            print(e)

        # Declare member variables for modules in the maq20 system.
        self.maq20 = None  # type: MAQ20
        self.jtc = None  # type: MAQ20Module
        self.vdn = None  # type: MAQ20Module
        self.vo = None  # type: outputmodule.OutputModule
        self.diol = None  # type: diol.DIOL
        self._timer = None  # type: QTimer

        # Try to initialize on startup.
        self.init_maq20()
        self.led_bar_control_checkbox.toggle()

    @pyqtSlot()
    def init_maq20(self):
        """
        Initializes the MAQ20 system. Because this example is designed to work with the Demo suitcase, it expects 
        to see a JTC, VDN, VO, and DIOL modules.
        After initializing MAQ20, this function starts a timer that is connected to tick()
        :return: no return
        """
        self.status_line.setText("Connecting, please wait.")
        self.connection_switch.setValue(0)
        try:
            self.maq20 = MAQ20(ip_address=self.ip_address_line.displayText(), port=self.port_spinbox.value())
            self.jtc = self.maq20.find("JTC")
            self.vdn = self.maq20.find("VDN")
            dio = self.maq20.find("DIOL")
            self.vo = self.maq20.find("VO")
            self.diol = diol.DIOL(dio)
            self._timer = QTimer()
            self._timer.timeout.connect(self.tick)
            self._timer.start(50)
            self.status_line.setText("Connected to {}".format(self.ip_address_line.displayText()))
            self.connection_switch.setValue(1)
        except Exception as e:
            print(e)
            self.status_line.setText("No Connection")

    @pyqtSlot(float)
    def internal_tc_heat_1(self, p_double):
        try:
            self.vo.write_channel_data(channel=4, data=p_double)
        except Exception as e:
            print(e)

    @pyqtSlot(float)
    def internal_tc_heat_2(self, p_double):
        try:
            self.vo.write_channel_data(channel=5, data=p_double)
        except Exception as e:
            print(e)

    @pyqtSlot(int)
    def freq_slider_val(self, p_int):
        try:
            self.diol.write_special_function_5_frequency_generator(timer=0, frequency=p_int)
        except Exception as e:
            print(e)

    @pyqtSlot(int)
    def vout1_slider_val(self, p_int):
        try:
            self.vo.write_channel_data(channel=0, data=p_int)
        except Exception as e:
            print(e)

    @pyqtSlot(int)
    def vout2_slider_val(self, p_int):
        if not self.led_bar_control_checkbox.isChecked():
            self.led_bar_control_checkbox.toggle()
        try:
            self.vo.write_channel_data(channel=2, data=p_int)
        except Exception as e:
            print(e)

    @pyqtSlot(int)
    def vout3_slider_val(self, p_int):
        if not self.led_bar_control_checkbox.isChecked():
            self.led_bar_control_checkbox.toggle()
        try:
            self.vo.write_channel_data(channel=3, data=p_int)
        except Exception as e:
            print(e)

    @pyqtSlot(bool)
    def led_control(self, p_bool):
        try:
            if p_bool:
                self.vo.write_channel_data(channel=1, data=10)
            else:
                self.vo.write_channel_data(channel=1, data=-10)
        except Exception as e:
            print(e)

    @pyqtSlot(int)
    def motor_pot_1_val(self, p_int):
        try:
            self._timer.blockSignals(True)
            if self.led_bar_control_checkbox.isChecked():
                self.led_bar_control_checkbox.toggle()
            message = QMessageBox()
            message.setIcon(QMessageBox.Warning)
            message.setText("Moving Knob. Please Wait.              ")
            message.setWindowTitle("Motor Pot Rotating. Please Wait.")
            message.show()
            attempts_limit = 200
            attempts = 0
            new_value = p_int / (20/3.3)
            current_value = self.vdn.read_channel_data(channel=1)
            while not (new_value-0.01 < current_value < new_value+0.01) and attempts < attempts_limit:
                if new_value > current_value:  # FWD
                    self.diol.write_channel_data(1, 1)
                    self.diol.write_channel_data(2, 0)
                else:  # REV
                    self.diol.write_channel_data(1, 0)
                    self.diol.write_channel_data(2, 1)
                self.vo.write_channel_data(6, 10)
                time.sleep(.05)
                self.vo.write_channel_data(6, -1)
                # update variables
                current_value = self.vdn.read_channel_data(channel=1)
                attempts += 1
            self._timer.blockSignals(False)
            self.diol.write_channel_data(1, 0)
            self.diol.write_channel_data(2, 0)
            message.destroy()
        except Exception as e:
            print(e)

    @pyqtSlot(int)
    def motor_pot_2_val(self, p_int):
        try:
            self._timer.blockSignals(True)
            if self.led_bar_control_checkbox.isChecked():
                self.led_bar_control_checkbox.toggle()
            message = QMessageBox()
            message.setIcon(QMessageBox.Warning)
            message.setText("Moving Knob. Please Wait.              ")
            message.setWindowTitle("Motor Pot Rotating. Please Wait.")
            message.show()
            attempts_limit = 200
            attempts = 0
            new_value = p_int / (20 / 3.3)
            current_value = self.vdn.read_channel_data(channel=2)
            while not (new_value - 0.01 < current_value < new_value + 0.01) and attempts < attempts_limit:
                if new_value > current_value:  # FWD
                    self.diol.write_channel_data(3, 1)
                    self.diol.write_channel_data(4, 0)
                else:  # REV
                    self.diol.write_channel_data(3, 0)
                    self.diol.write_channel_data(4, 1)
                self.vo.write_channel_data(7, 10)
                time.sleep(.05)
                self.vo.write_channel_data(7, -1)
                # update variables
                current_value = self.vdn.read_channel_data(channel=2)
                attempts += 1
            self._timer.blockSignals(False)
            self.diol.write_channel_data(3, 0)
            self.diol.write_channel_data(4, 0)
            message.destroy()
        except Exception as e:
            print(e)

    @pyqtSlot()
    def tick(self):
        try:
            self._update_int_tc_heat()
            self._update_switches()
            self._update_tc_external()
            if self.led_bar_control_checkbox.isChecked():
                self._update_sliders()
            else:
                self._update_motors()
        except Exception as e:
            print(e)

    def _update_int_tc_heat(self):
        try:
            tc_heat_1 = self.vo.read_channel_data(channel=4)
            tc_heat_2 = self.vo.read_channel_data(channel=5)
            old_value = self.tc_heat_1_spinbox.blockSignals(True)
            self.tc_heat_1_spinbox.setValue(tc_heat_1)
            self.tc_heat_1_spinbox.blockSignals(old_value)
            old_value = self.tc_heat_2_spinbox.blockSignals(True)
            self.tc_heat_2_spinbox.setValue(tc_heat_2)
            self.tc_heat_2_spinbox.blockSignals(old_value)
            self.int_tc_spinbox_indicator.setValue(self.jtc.read_channel_data(6))
        except Exception as e:
            print(e)

    def _update_switches(self):
        values = self.diol.read_data(5, 5)
        self.sw1.setChecked(values[0] ^ 1)
        self.sw1_slider.setValue(values[0] ^ 1)
        self.sw2.setChecked(values[1] ^ 1)
        self.sw2_slider.setValue(values[1] ^ 1)
        self.sw3.setChecked(values[2] ^ 1)
        self.sw3_slider.setValue(values[2] ^ 1)
        self.sw4.setChecked(values[3] ^ 1)
        self.sw4_slider.setValue(values[3] ^ 1)
        self.sw5.setChecked(values[4] ^ 1)
        self.sw5_slider.setValue(values[4] ^ 1)

    def _update_tc_external(self):
        module_channel = 7
        ext_temperature = self.jtc.read_channel_data(module_channel)
        self.tc_touch_line_edit.setText('{} {}'.format(ext_temperature, self.jtc.get_engineering_units(module_channel)))

    def _update_sliders(self):
        frequency = self.diol.read_register(1105)
        self.freq_spinbox.setValue(frequency/1000.0)
        self.freq_slider.setValue(frequency)
        voltages = self.vo.read_data(0, 4)
        self.vout1_spinbox.setValue(voltages[0])
        self.vout1_slider.setValue(round(voltages[0]))
        self.vout2_spinbox.setValue(voltages[2])
        old_state = self.vout2_slider.blockSignals(True)
        self.vout2_slider.setValue(round(voltages[2]))
        self.vout2_slider.blockSignals(old_state)
        self.vout3_spinbox.setValue(voltages[3])
        old_state = self.vout3_slider.blockSignals(True)
        self.vout3_slider.setValue(round(voltages[3]))
        self.vout3_slider.blockSignals(old_state)

    def _update_motors(self):
        values = self.vdn.read_data(start_channel=1, number_of_channels=2)
        old_value = self.motor_pot_1.blockSignals(True)
        self.motor_pot_1.setValue(round(values[0]*(20.0/3.3)))
        self.motor_pot_1.blockSignals(old_value)
        old_value = self.motor_pot_2.blockSignals(True)
        self.motor_pot_2.setValue(round(values[1]*(20.0/3.3)))
        self.motor_pot_2.blockSignals(old_value)
        old_state = self.vout2_slider.blockSignals(True)
        self.vout2_slider.setValue(round(values[0]*(20.0/3.3)-10))
        self.vout2_slider.blockSignals(old_state)
        old_state = self.vout3_slider.blockSignals(True)
        self.vout3_slider.setValue(round(values[1] * (20.0 / 3.3) - 10))
        self.vout3_slider.blockSignals(old_state)

    @pyqtSlot()
    def copyright(self):
        message = QMessageBox(self)
        message.setText(
            """Copyright 2017 Dataforth Corporation
All Rights Reserved."""
        )
        message.setWindowTitle('About')
        message.show()


if __name__ == '__main__':
    import sys
    # make_ui()
    app = QApplication(sys.argv)
    ui = DemoBox()
    ui.show()
    sys.exit(app.exec_())
