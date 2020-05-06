import gpiozero
import time
import math


class Robocar:
    def __init__(self):
        self._motor_front_left = gpiozero.Motor(forward=6, backward=5)
        self._motor_front_right = gpiozero.Motor(forward=12, backward=13)
        self._motor_back_left = gpiozero.Motor(forward=16, backward=19)
        self._motor_back_right = gpiozero.Motor(forward=20, backward=26)
        self._horn = gpiozero.LED(4)

    def honk(self):
        self._horn.on()
        time.sleep(0.2)
        self._horn.off()

    def horn_on(self):
        self._horn.on()

    def horn_off(self):
        self._horn.off()

    def self_test(self):
        self.honk()
        motors = [self._motor_front_left, self._motor_front_right,\
                self._motor_back_right, self._motor_back_left]
        for motor in motors:
            motor.forward()
            time.sleep(0.1)
            motor.stop()
            time.sleep(0.1)
            motor.backward()
            time.sleep(0.1)
            motor.stop()
            time.sleep(0.1)
        self.honk()

    def set_motor_speed(self, motor, speed):
        if abs(speed) > 1.0:
            speed = math.copysign(1.0, speed)
        min_speed = 0.4
        if abs(speed) < min_speed:
            speed = 0.0
        if speed > 0:
            motor.forward(speed)
        else:
            motor.backward(-speed)

    def set_speed(self, linear, angular):
        wheel_base = 2.0
        left_speed = linear + 0.5 * wheel_base * angular
        right_speed = linear - 0.5 * wheel_base * angular
        self.set_motor_speed(self._motor_front_left, left_speed)
        self.set_motor_speed(self._motor_back_left, left_speed)
        self.set_motor_speed(self._motor_front_right, right_speed)
        self.set_motor_speed(self._motor_back_right, right_speed)

