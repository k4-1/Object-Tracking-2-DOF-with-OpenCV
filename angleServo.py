from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def setServoAngle(servo, angle):
	pwm = GPIO.PWM(servo, 50)
	pwm.start(8)
	dutyCycle = angle / 18. + 3.
	pwm.ChangeDutyCycle(dutyCycle)
	sleep(0.5)
	pwm.stop()

if __name__ == '__main__':
	import sys
	servo = int (17)
	GPIO.setup(servo, GPIO.OUT)
	setServoAngle(servo, int(90))
	GPIO.cleanup()