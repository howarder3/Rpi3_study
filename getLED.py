from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import time 
import RPi.GPIO as GPIO

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# set up GPIO output channel, we set GPIO4 (Pin 7) to OUTPUT
GPIO.setup(7, GPIO.OUT)

SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))

# Call the Sheets API
SPREADSHEET_ID = '1RaGPlEJKQeg_xnUGi1mlUt95-Gc6n-XF_czwudIP5Qk'
RANGE_NAME = 'LED!A1:B1'
value_input_option = 'USER_ENTERED'

def get_LED_state():
	result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,range=RANGE_NAME).execute()
	values = result.get('values', [])
	LED = 0
	if not values:
		print('No data found.')
	else:
		for row in values:
			LED = int(row[0])
		# Print columns A and E, which correspond to indices 0 and 4.
		print(LED)
		return LED

# blinking function
def blink(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    return

def LED_on():
	pin = 7
	GPIO.output(pin,GPIO.HIGH)
	return

def LED_off():
	pin = 7
	GPIO.output(pin,GPIO.LOW)
	return

LED_signal = 0
while(LED_signal >= 0):
	LED_signal = get_LED_state()
	if(LED_signal == 1):
		LED_on()
	elif(LED_signal == 0):
		LED_off()
	time.sleep(3)

GPIO.cleanup()
	
# blink GPIO4 (Pin 7) 50 times
# for i in range(0,50):
#     blink(7)

