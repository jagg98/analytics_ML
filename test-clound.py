__author__ = "Alejandro Garcia"
__version__ = "1.0"
import socket
import sys
import RPi.GPIO as GPIO

#define the ping that we use

LED_IOPIN = 24 #The led
LIGHT_IOPIN = 23 #light sensor

#DEFINE THE FEATURES OF US GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_IOPIN, GPIO.OUT)
GPIO.setup(LIGHT_IOPIN, GPIO.IN)

ADDR = ''
PORT = 10000
device_id = ""

#Create a UPD socket (Client)

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_add = (ADDR, PORT)










if __name__ == '__main__':
    if not device_id:
        sys.exit('Device no identify')
    
