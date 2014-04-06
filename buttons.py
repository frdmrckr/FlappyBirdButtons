'''
Created on Apr 4, 2014

@author: Mike Campbell
'''
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate
from time import sleep
import time


lcd = Adafruit_CharLCDPlate()
lcd.begin(16, 2)
lcd.clear()
lcd.backlight(lcd.ON)
btn = (lcd.LEFT, lcd.UP, lcd.DOWN, lcd.RIGHT, lcd.SELECT)
score = 0
highscore=0
state = "new"
secs=0
inittime=0

def Highscore(score,highscore):
    if score > highscore:
        highscore = score
    return highscore
    
    

while True:
    
    if state == "playing":
        secs=time.time()-inittime
        lcd.setCursor(11, 0)
        lcd.message("Time:")
        lcd.setCursor(11,1)
        lcd.message(secs)
        t=secs
    
    if state == "pause":
        t = t
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
                if state != "pause":
                    if lcd.buttonPressed(btn[4]):
                        score = score
                    else:
                        if score == 0:
                            lcd.clear()
                            inittime=time.time()
                        score +=1
                        highscore = Highscore(score,highscore)
                        lcd.setCursor(0,0)
                        lcd.message("Score:"+str(score)+"\n"+"High:"+str(highscore))
                        state ="playing"
            if b is btn[3]:
                score = 0
                lcd.clear()
                lcd.message("Game Reset")
                state="new"
                sleep(1)

            if b is btn[0]:
                if state =="playing":
                    state="pause"
                elif state =="pause":
                    inittime=time.time()
                    state="playing"