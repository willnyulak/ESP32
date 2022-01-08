# MicroPython SH1106 OLED driver
#
# Pin Map I2C for ESP8266
#   - 3v - xxxxxx   - Vcc
#   - G  - xxxxxx   - Gnd
#   - D2 - GPIO 5   - SCK / SCL
#   - D1 - GPIO 4   - DIN / SDA
#   - D0 - GPIO 16  - Res (required, unless a Hardware reset circuit is connected)
#   - G  - xxxxxx     CS
#   - G  - xxxxxx     D/C
#
# Pin's for I2C can be set almost arbitrary
#
from machine import Pin, SoftI2C
import sh1106
import dht

d=dht.DHT11(Pin(15, Pin.IN))
t=d.temperature()
h=d.humidity()
i2c = SoftI2C(scl=Pin(19), sda=Pin(21), freq=400000)
display = sh1106.SH1106_I2C(128, 64, i2c, Pin(16), 0x3c)

display.sleep(False)
display.fill(0)
# four lines of test text almost perfectly centered and aligned
display.text('Measurements', 25, 4, 1)
display.text('Temperature', str(t), 5, 20, 1)
display.text('Humidity', str(h), 25, 36, 1)
display.text('Testing 4', 25, 52, 1)
display.show()