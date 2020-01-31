# -*- coding: utf-8 -*-

# script Raspberry
from picamera import PiCamera
from gpiozero import MotionSensor
from datetime import datetime
from time import sleep
import smtplib
import os

gmail_user = '' # TODO: email address
gmail_password = '' # TODO: email password

camera = PiCamera()
pir = MotionSensor(4) # pin GPIO

destination = '/home/pi/Videos' # path

camera.rotation = 180

while True:
	settings = open('settings.txt', 'r+') # open file
	line = settings.readlines() # get line to variables
	settings.close() # close file

	pir.wait_for_motion()
	file = os.path.join(destination, datetime.now().strftime("pb_%Y-%m-%d_%H.%M.%S.h264"))

	camera.start_recording(file)
	sleep(float(line[0]))
	camera.stop_recording()

	sent_from = gmail_user
	to = [''] # TODO: email to send alert
	subject = "Warning!"
	body = "Motion was detected around the camera, the recording was saved to file: "+file
	email_text = """
	From: %s
	To: %s
	Subject: %s

	%s
	""" % (sent_from, to, subject, body)

	try:  
	    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	    server.ehlo()
	    server.login(gmail_user, gmail_password)
	    server.sendmail(sent_from, to, email_text)
	    server.close()
	    print ("Email sent")
	except:  
	  print ("Something is wrong!")

	del settings
	del line
	del file
