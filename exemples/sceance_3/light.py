from gpiozero import LightSensor
from time import sleep


# set this to 0.01 if 1uF capacitor or 0.03 if 4.7 ²uF
charge_time_limit=0.03
ldr = LightSensor(21, charge_time_limit=charge_time_limit)


def on():
    print("on")

def off():
    print("off")

ldr.when_dark = on
ldr.when_light = off


last_value = 0
while True:
    sleep(0.2)
    current = round(ldr.value, 2)
    if last_value != current:
        print(current)
        last_value = current
    
