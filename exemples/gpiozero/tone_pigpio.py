from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from gpiozero.pins.pigpio import PiGPIOFactory
import time
factory = PiGPIOFactory()
t = TonalBuzzer(23, pin_factory=factory)
t.play(Tone(440))
time.sleep(3)
t.stop()
