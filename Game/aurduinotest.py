import serial
import socket


Arduino = serial.Serial('COM8',9600)
opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    if Arduino.readline():
        print("yo")

        arduinoInput = Arduino.readline()
        if ('up' in arduinoInput.decode('utf-8')) or ('down' in arduinoInput.decode('utf-8')) or ('space' in arduinoInput.decode('utf-8')):
            opened_socket.sendto(arduinoInput, ("127.0.0.1", 15006))
