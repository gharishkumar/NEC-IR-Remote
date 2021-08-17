import RPi.GPIO as GPIO
from datetime import datetime

pin = 5
Buttons = [0x300ff28d7,0x300ff08f7,0x300ff10ef,0x300ff12ed,0x300ff926d,0x300ff52ad,0x300fff00f,0x300ff50af,0x300ff7887,0x300ff42bd,0x300ffc837,0x300ff8a75,0x300ffc03f,0x300ff40bf,0x300ff609f,0x300ffe21d,0x300ffe01f,0x300ff02fd,0x300ffa25d,0x300ff22dd,0x300ff7a85,0x300ffc23d,0x300ff4ab5,0x300ffd22d,0x300ff629d,0x300ff906f,0x300ffb847,0x300fff807,0x300ffb04f,0x300ff9867,0x300ffd827,0x300ff8877,0x300ffa857,0x300ffe817,0x300ff48b7,0x300ff9a65,0x300ff827d,0x300ffda25,0x300ff6897,0x300ff708f,0x300ff58a7]
ButtonsNames = ["POWER","BUZ.MUTE","C","E","SNELLAN","LOGMAR","NUMERICS",  "ALPHABETS","RED/GREEN","MADDOX","CONTRAST","PERIPHERALS","ISHIHARA","ACC","UP","LEFT","ENTER","RIGHT","MEDIA MUTE","DOWN","BACK","SETTINGS","LANG-1","LANG-2","MEDIA","SC1","SC2","SC3","SC4","ASTIG FAN","DOTS","PEDIATRIC","CARTOON","ANIMALS","LAN-1","LAN-2","EDUCATION","NOP 1","NOP 2","VOL-","VOL+"]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN)

def getBinary():
	num1s = 0
	binary = 1
	command = []
	previousValue = 0
	value = GPIO.input(pin)
	
	while value:
		value = GPIO.input(pin)
	
	startTime = datetime.now()
	
	while True:
		if previousValue != value:
			now = datetime.now()
			pulseTime = now - startTime
			startTime = now
			command.append((previousValue, pulseTime.microseconds))
		
		if value:
			num1s += 1
		else:
			num1s = 0
		
		if num1s > 10000:
			break
		
		previousValue = value
		value = GPIO.input(pin)
	
	for (typ, tme) in command:
		if typ == 1:
			if tme > 1000:
				binary = binary *10 +1
			else:
				binary *= 10
			
	if len(str(binary)) > 34:
		binary = int(str(binary)[:34])
		
	return binary

def convertHex(binaryValue):
	tmpB2 = int(str(binaryValue),2)
	return hex(tmpB2)

while True:
	inData = convertHex(getBinary())
	for button in range(len(Buttons)):
		if hex(Buttons[button]) == inData:
			print(ButtonsNames[button])
			