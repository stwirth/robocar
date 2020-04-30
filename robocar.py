import gpiozero
import time


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

    def test_motors(self):
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

    def set_motor_speed(self, motor, speed):
        if abs(speed) > 1.0:
            speed = math.copysign(1.0, speed)
        if speed > 0:
            motor.forward(speed)
        else:
            motor.backward(speed)

    def set_speed(self, linear, angular):
        self.set_motor_speed(self._motor_front_left, linear)
        self.set_motor_speed(self._motor_front_right, linear)
        self.set_motor_speed(self._motor_back_left, linear)
        self.set_motor_speed(self._motor_back_right, linear)


robocar = Robocar()
robocar.honk()
robocar.set_speed(1.0, 0.0)
time.sleep(1.0)
robocar.set_speed(0.0, 0.0)

