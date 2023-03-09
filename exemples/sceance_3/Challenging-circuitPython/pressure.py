import time
import board
import adafruit_bmp280


# Create sensor object, using the board's default I2C bus.
i2c = board.I2C()
sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)

# change this to match the location's pressure (hPa) at sea level
sensor.sea_level_pressure = 1013.25

while True:
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Pressure: %0.1f hPa" % sensor.pressure)
    print("Altitude = %0.2f meters" % sensor.altitude)
    time.sleep(2)

