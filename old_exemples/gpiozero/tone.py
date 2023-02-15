from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
import time

t = TonalBuzzer(23)
t.play(Tone(440))
time.sleep(3)
t.play(Tone(240))
time.sleep(3)
t.play(Tone(540))
t.stop()
