'''
Created on Apr 4, 2014

@author: Mike Campbell
'''
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
import time

sleep=time.sleep()
lcd = Adafruit_CharLCDPlate()
lcd.begin(16, 2)
lcd.clear()
lcd.backlight(lcd.ON)
btn = (lcd.LEFT, lcd.UP, lcd.DOWN, lcd.RIGHT, lcd.SELECT)
score = 0
highscore=0
state = "new"
time=0

def Highscore(score,highscore):
    if score > highscore:
        highscore = score
    return highscore
    
    

while True:
    
    if state == "playing":
        if score == 0:
            inittime=time.clock()
        else:
            time=time.clock()-inittime
    if state == "new":
        lcd.clear()
        lcd.message("Sparty Bird!")
        state ="start"
        sleep(1)
        lcd.clear()
        lcd.message("Ready to Play!")
    
    for b in btn:
        if lcd.buttonPressed(b):
            if b is btn[4]:
                sleep(.2)
                if lcd.buttonPressed(btn[4]):
                    score = score
                else:
                    score +=1
                    highscore = Highscore(score,highscore)
                    lcd.clear()
                    lcd.message("Score:"+str(score)+"\n"+"Highscore:"+str(highscore))
                    state ="playing"
            if b is btn[3]:
                score = 0
                lcd.clear()
                lcd.message("Game Reset")
                state="new"
                sleep(1)
    lcd.setCursor(12, 1)
    lcd.message(time)
            