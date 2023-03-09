from gpiozero import MotionSensor
from signal import pause

pir = MotionSensor(21)

def motion():
    print("Motion detected!")

def noMotion():
    print("______________")


pir.when_motion = motion
pir.when_no_motion = noMotion


pause()
