import RPi.GPIO as GPIO
from time import sleep

# disable warnings (optional)
GPIO.setwarnings(False)

# Select GPIO Mode
GPIO.setmode(GPIO.BCM)

# set red,green, blue
relay = 25

# set pins as outputs
GPIO.setup(relay, GPIO.OUT)


def turnOff():
    GPIO.output(relay, GPIO.LOW)


def turnOn():
    GPIO.output(relay, GPIO.HIGH)


def main():
    while True:
        turnOn()
        sleep(5)
        turnOff()
        sleep(5)


try:
    main()
except KeyboardInterrupt:
    turnOff()
    print('Thanks!\n')
