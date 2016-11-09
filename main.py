from tkinter import *
from tkinter import messagebox
import RPi.GPIO as GPIO
import time
from telegram import Telegram
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
GPIO.setup(7,GPIO.IN)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

root = Tk()
flash = False
speed = 1
w = {}
time.sleep(speed/100)
tg = Telegram()
tguser = '6435514'

def buttonclick():
    global flash
    wachtwoord=w['pw'].get()

   #snel=snelheid.get()
    #print(snel)
    if wachtwoord == "test":
        GPIO.output(15, False)
        tg.sendMessage("Alarm gedeactiveerd!", tguser)
        flash = False
        w['enterPw'].pack_forget()
        w['pw'].delete(0, 'end')
        w['pw'].pack_forget()
        w['enterPw'].pack_forget()
        w['button'].pack_forget()
        w['speedScale'].pack()
        w['speed'].pack()
        w['speedbutton'].pack()
    else:
        messagebox.showinfo("Wachtwoord Incorrect","Probeer het nog een keertje :)")
def checkTrigger():
    global flash
    if GPIO.input(11) == 1:
        flash = True
        tg.sendMessage("Alarm geactiveerd!", tguser)
def checkDeactivate():
    global flash
    global w
    if GPIO.input(7) == 1 and flash == True:
        GPIO.output(15, True)
        w['enterPw'].pack()
        w['pw'].pack()

        w['enterPw'].pack()

        w['button'].pack()
def flashLed():
    global flash
    if flash == True:
        GPIO.output(13, True)
        time.sleep(speed/80)
        GPIO.output(13, False)
        time.sleep(speed/80)


def setSpeed():
    global speed
    speed = w['speedScale'].get()

    w['speedScale'].pack_forget()
    w['speed'].pack_forget()
    w['speedbutton'].pack_forget()
    
def main():
    checkTrigger()
    checkDeactivate()
    flashLed()
    
    

w['enterPw'] = Label(master=root, text='Voer het wachtwoord in', height=2)

w['pw'] = Entry(master=root, show="*")

w['speed']=Label(master=root,text='Snelheid')

w['speedScale'] = Scale(master=root, from_=1, to=10,orient=HORIZONTAL)

w['button']=Button(master=root,text='Voer in',command=buttonclick)

w['speedbutton']=Button(master=root,text='Stel in',command=setSpeed)
while True:
        root.update_idletasks()
        root.update()
        main()
