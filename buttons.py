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
secs=0.000
inittime=0

def Highscore(score,highscore):
    if score > highscore:
        highscore = score
    return highscore

def writeScore(score,highscore):
    lcd.setCursor(0,0)
    lcd.message("Score:"+str(score)+"\n"+"High:"+str(highscore))
    return

def writeTime(secs):
    lcd.setCursor(11, 0)
    lcd.message("Time:")
    lcd.setCursor(11,1)
    lcd.message(secs)
    return
    

while True:
    
    if state == "playing":
        secs=time.time()-inittime
        writeTime(secs)
        t=secs
    
    if state == "pause":
        t=t
        
    if state == "new":
        lcd.clear()
        writeScore(score,highscore)
        writeTime(secs)
        state=("ready")
    
    for b in btn:
        if lcd.buttonPressed(b):
            if b is btn[4]:
                sleep(.2)
                if state != "pause":
                    if lcd.buttonPressed(btn[4]):
                        score = score
                    else:
                        if state == "ready":
                            score=1
                            state="playing"
                            lcd.clear()
                            writeScore(score,highscore)
                            inittime=time.time()
                        else:
                            score +=1
                            highscore = Highscore(score,highscore)
                            writeScore(score,highscore)
            if b is btn[3]:
                state="new"
                sleep(.2)