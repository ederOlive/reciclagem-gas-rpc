#!/bin/bash

# Set the serial device and baud rate
SERIAL_DEVICE="/dev/ttyACM0"
BAUD_RATE=9600

# Configure the serial port
stty -F $SERIAL_DEVICE $BAUD_RATE

# Read from the serial device and plot using ttyplot
cat $SERIAL_DEVICE | ttyplot -t "Leitura do sensor de pressão" -u "mbar"

# Versão que que não apaga o gráfico da tela quando o termina
#cat $SERIAL_DEVICE | TERM=vt100 ttyplot -t "Leitura do sensor de pressão" -u "mbar"

