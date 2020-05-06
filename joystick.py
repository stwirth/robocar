import evdev
import asyncio
import time

## Some helpers ##
def scale(val, src, dst):
    """
    Scale the given value from the scale of src to the scale of dst.

    val: float or int
    src: tuple
    dst: tuple

    example: print(scale(99, (0.0, 99.0), (-1.0, +1.0)))
    """
    return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]

def scale_stick(value):
    return scale(value,(0,255),(-100,100))


class Joystick():
    def __init__(self):
        self._device = None
        self._axes = [0] * 6
        self._buttons = [0] * 17
        self._axes_codes = [
                evdev.ecodes.ABS_X,
                evdev.ecodes.ABS_Y,
                evdev.ecodes.ABS_Z,
                evdev.ecodes.ABS_RX,
                evdev.ecodes.ABS_RY,
                evdev.ecodes.ABS_RZ,
                ]
        self._button_codes = [
                evdev.ecodes.BTN_SOUTH
                ]

    def is_connected(self):
        return self._device is not None

    def connect(self):
        self._device = None
        print("Trying to find PS3 controller...")
        all_devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        for device in all_devices:
            print(device.name)
            if device.name == 'Sony PLAYSTATION(R)3 Controller':
                self._device = evdev.InputDevice(device.path)
                break
        return self._device is not None

    def get_state(self):
        return self._buttons, self._axes

    def update_state(self, event):
        if event.type == evdev.ecodes.EV_KEY:
            if event.code in self._button_codes:
                self._buttons[self._button_codes.index(event.code)] = event.value
        if event.type == evdev.ecodes.EV_ABS:
            if event.code in self._axes_codes:
                self._axes[self._axes_codes.index(event.code)] = scale_stick(event.value)

    async def listen(self, cb):
        async for ev in self._device.async_read_loop():
            self.update_state(ev)
            buttons, axes = self.get_state()
            cb(buttons, axes)


if __name__ == '__main__':

    def cb(buttons, axes):
        print('buttons: ', buttons, ' axes: ', axes)

    try:
        joy = Joystick()
        while True:
            if not joy.is_connected():
                time.sleep(1)
                joy.connect()
            else:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(joy.listen(cb))
    except KeyboardInterrupt:
        pass

