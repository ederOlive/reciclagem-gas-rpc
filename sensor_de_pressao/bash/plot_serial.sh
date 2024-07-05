#!/bin/bash

# Set the serial device and baud rate
SERIAL_DEVICE="/dev/ttyACM0"
BAUD_RATE=9600

# Configure the serial port
stty -F $SERIAL_DEVICE $BAUD_RATE

# Read from the serial device and plot using ttyplot
cat $SERIAL_DEVICE | ttyplot -t "Sensor de pressão HSCDDRN060MD2A5 (Honeywell)" -u "mbar"

