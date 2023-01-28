import gpiozero
import time
import math


class Robocar:
    def __init__(self):
        self._motor_right = gpiozero.Motor(forward=12, backward=13)
        self._motor_left = gpiozero.Motor(forward=5, backward=6)
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
        motors = [self._motor_left, self._motor_right]
        for motor in motors:
            print('forward')
            motor.forward()
            time.sleep(0.5)
            print('stop')
            motor.stop()
            time.sleep(0.5)
            print('backward')
            motor.backward()
            time.sleep(0.5)
            print('stop')
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
        self.set_motor_speed(self._motor_left, left_speed)
        self.set_motor_speed(self._motor_right, right_speed)

