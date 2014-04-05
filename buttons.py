'''
Created on Apr 4, 2014

@author: Mike Campbell
'''
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from time import sleep

lcd = Adafruit_CharLCDPlate()
lcd.begin(16, 2)
lcd.clear()
lcd.backlight(lcd.ON)
btn = (lcd.LEFT, lcd.UP, lcd.DOWN, lcd.RIGHT, lcd.SELECT)
score = 0
state = "new"

while True:
    
    if state == "new":
        lcd.message("Sparty Bird!")
        sleep(1)
    
    for b in btn:
        if lcd.buttonPressed(b):
            if b is btn[4]:
                score +=1
                lcd.clear()
                lcd.message("Score:"+score)
                state ="playing"
                sleep(.05)
            if b is btn[3]:
                score = 0
                lcd.clear()
                lcd.message("Game Reset")
                state="new"
                sleep(.2)

            