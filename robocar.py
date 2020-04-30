import gpiozero
import time


front_left = gpiozero.Motor(forward=6, backward=5)
front_right = gpiozero.Motor(forward=12, backward=13)
back_left = gpiozero.Motor(forward=16, backward=19)
back_right = gpiozero.Motor(forward=20, backward=26)

horn = gpiozero.LED(4)

horn.on()
time.sleep(0.1)
horn.off()

front_left.forward()
time.sleep(0.5)
front_left.stop()

front_right.forward()
time.sleep(0.5)
front_right.stop()

back_right.forward()
time.sleep(0.5)
back_right.stop()

back_left.forward()
time.sleep(0.5)
back_left.stop()


