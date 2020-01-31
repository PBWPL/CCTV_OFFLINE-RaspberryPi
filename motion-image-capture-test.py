import RPi.GPIO as GPIO
import picamera
import time
camera = picamera.PiCamera()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN) # motion sensor
GPIO.setup(3, GPIO.OUT) # LED
j=0;

while True:
       i=GPIO.input(11)
       if i==0:
             print "no motion detected",i
             GPIO.output(3, 0)
             time.sleep(0.5)
       elif i==1:
             print "motion detected",i
             GPIO.output(3, 1) # LED on
             j=j+1
             camera.capture('image%03d.jpg'%j) # image capture
			 time.sleep(0.5)
