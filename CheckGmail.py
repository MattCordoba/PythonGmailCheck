##*****************************************************************************************************
## Author: Matt Cordoba
## Email: cordobamatt@gmail.com
## Date: 16/07/2013
## Purpose: Checks a users Gmail Account for messages. If the new message contains the phrase "#makecoffee"
## then it will write a byte to the serial port.  Receive this byte on your microcontroller board to 
## perform an action
##*****************************************************************************************************

import imaplib
import serial
import email
import time
def searchGmail():
	print "Welcome to Gmail-Coffee"
	time.sleep(1)
	print "System intialization"
	#Connect to Gmail Account
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login('[your_email]', '[your_password]')
	mail.list()
	# Out: list of "folders" aka labels in gmail.
	mail.select("inbox") # connect to inbox.
	result, data = mail.uid('search', None, "ALL") # searpych and return uids instead
	latest_email_uid = data[0].split()[-1]
	result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
	raw_email = data[0][1]
	email_message = email.message_from_string(raw_email)
	#assign a default value in case no body in email
	message_body = "#nocoffee"
	for part in email_message.walk():
	    #only assign the body of the message
	    if part.get_content_type() == 'text/plain':
	         message_body = part.get_payload() 
	time.sleep(1)
	print "Message Received: "
	time.sleep(1)
	print message_body
	time.sleep(1)

	#intialize serial port so we can write to it
	port = 'COM4'
	usb = serial.Serial('COM4', 19200)
	time.sleep(3)


	if "#makecoffee" in message_body:
		usb.write('1')
		print "Command to make coffee found!"
		time.sleep(1)
		print "Making Coffee"
		time.sleep(1)
		print "....."
		time.sleep(1)
		print "....."
	else:
		#usb.write('0')
		print "Command: stop making coffee"
		time.sleep(1)
		print "Turning off coffee"
		time.sleep(1)
		print"....."
		time.sleep(1)
		print "....."

while 1:
	searchGmail()
	time.sleep(60 * 10)