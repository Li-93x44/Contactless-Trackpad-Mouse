# main.py - Core Air-Mouse & Gesture Trackpad Loop
from machine import Pin, I2C
import time
import ssd1306

# Initialize I2C (using GPIO 4 for SDA, GPIO 5 for SCL - adjust if wired differently)
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

# Initialize OLED Display (128x64 resolution)
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Display startup message
display.fill(0)
display.text("Fallen Air-Mouse", 0, 0, 1)
display.text("Initializing...", 0, 16, 1)
display.show()

time.sleep(1)

# Main runtime loop
try:
    while True:
        # Clear display buffer for next frame
        display.fill(0)
        
        # Status header
        display.text("Fallen Air-Mouse", 0, 0, 1)
        display.text("Status: Active", 0, 16, 1)
        
        # Update screen
        display.show()
        
        time.sleep(0.1)
        
except KeyboardInterrupt:
    display.fill(0)
    display.text("Stopped", 0, 0, 1)
    display.show()