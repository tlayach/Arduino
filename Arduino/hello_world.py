import serial

if __name__ == "__main__":
    PORT = "/dev/cu.usbmodem411"  # "COM1"
    BAUD = 115200
    TIMEOUT = 0.1

    arduino = serial.Serial(port=PORT,
                            baudrate=BAUD,
                            timeout=TIMEOUT)

    while True:
        data = arduino.readline().strip()
        if data:
            print(f"Message from Arduino: {data}")

# Message from Arduino: b'Hello World!'
# Message from Arduino: b'Hello World!'
# Message from Arduino: b'Hello World!'
# ...
