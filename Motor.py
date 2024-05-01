import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor():
    def __init__(self, En, left, right):
        self.En = En
        self.left = left
        self.right = right
        GPIO.setup(En, GPIO.OUT)
        GPIO.setup(left, GPIO.OUT)
        GPIO.setup(right, GPIO.OUT)
        self.pwm = GPIO.PWM(En, 100)
        self.pwm.start(0)

    def forward(self, speed):
        GPIO.output(self.left, GPIO.HIGH)
        GPIO.output(self.right, GPIO.LOW)
        self.pwm.ChangeDutyCycle(speed)
    def backward(self, speed):
        GPIO.output(self.left, GPIO.LOW)
        GPIO.output(self.right, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(speed)
    def stop(self):
        GPIO.output(self.left, GPIO.LOW)
        GPIO.output(self.right, GPIO.LOW)
        self.pwm.ChangeDutyCycle(0)
    def left(self, speed):
        GPIO.output(self.left, GPIO.LOW)
        GPIO.output(self.right, GPIO.LOW)
        self.pwm.ChangeDutyCycle(speed)
    def right(self, speed):
        GPIO.output(self.left, GPIO.HIGH)
        GPIO.output(self.right, GPIO.HIGH)
        self.pwm.ChangeDutyCycle(speed)
    def cleanup(self):
        GPIO.cleanup()