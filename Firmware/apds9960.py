import time
from machine import Pin, I2C
from apds9960.const import *
from apds9960.device import APDS9960

i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
sensor = APDS9960(i2c)

# Gestures rely on proximity triggers, so we enable both
sensor.enableProximitySensor()
sensor.enableGestureSensor()

print("Waiting for gestures (Swipe your hand 5-10cm over the sensor)...")

# Mapping numeric response constants to human-readable strings
directions = {
    DIR_UP: "UP ↑",
    DIR_DOWN: "DOWN ↓",
    DIR_LEFT: "LEFT ←",
    DIR_RIGHT: "RIGHT →",
    DIR_NEAR: "NEAR ⊙",
    DIR_FAR: "FAR ⊗"
}

try:
    while True:
        if sensor.isGestureAvailable():
            motion = sensor.readGesture()
            if motion in directions:
                print("Gesture detected:", directions[motion])
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Stopping...")
