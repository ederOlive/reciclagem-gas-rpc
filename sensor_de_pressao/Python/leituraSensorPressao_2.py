import serial
import sys

def read_from_serial(port, baud_rate):
    try:
        # Open the serial port
        ser = serial.Serial(port, baud_rate, timeout=1)
        #print(f"Connected to {port} at {baud_rate} baud.", file=sys.stderr)

        # Continuously read data from the serial port
        while True:
            # Read a line of data from the serial port
            data = ser.readline().decode('utf-8').strip()
            if data:
                print(data)

    except serial.SerialException as e:
        print(f"Error: {e}", file=sys.stderr)
    except KeyboardInterrupt:
        print("Exiting...", file=sys.stderr)
    finally:
        if ser.is_open:
            ser.close()
            print(f"Closed connection to {port}", file=sys.stderr)

if __name__ == "__main__":
    # Set the serial port and baud rate
    port = "/dev/ttyACM0"  # Change this to your serial port
    baud_rate = 9600

    # Read data from the serial port and print it
    read_from_serial(port, baud_rate)
