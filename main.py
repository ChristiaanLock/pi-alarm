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
    """
    haalt het ww op en checkt of het goed is als het goed
    is wordt er een bericht gestuurd via telegram en worden
    de widgets weggehaald en nieuw widgets ingeladen
    """
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
    """
    Checkt of de knop gedrukt is en activeert het knipperende alarm
    """
    global flash
    if GPIO.input(11) == 1:
        flash = True
        tg.sendMessage("Alarm geactiveerd!", tguser)
def checkDeactivate():
    """als de andere knop geklikt wordt terwijl het alarm aan staat(flash == True)"""
    global flash
    global w
    if GPIO.input(7) == 1 and flash == True:
        GPIO.output(15, True)
        w['enterPw'].pack()
        w['pw'].pack()

        w['enterPw'].pack()

        w['button'].pack()
def flashLed():
    """dit is wat er gebeurt wanneer het lampje knippert"""
    global flash
    if flash == True:
        GPIO.output(13, True)
        time.sleep(speed/80)
        GPIO.output(13, False)
        time.sleep(speed/80)


def setSpeed():
    """zo wordt de snelheid van het knippere ingesteld
    de widgets om de instellingen te verkrijgen worden ingeladen
    en ze worden global gemaakt
    """
    global speed
    speed = w['speedScale'].get()

    w['speedScale'].pack_forget()
    w['speed'].pack_forget()
    w['speedbutton'].pack_forget()

def main():
    	"""dit het programma zelf als het ware deze functies worden continue gecontroleerd"""
    checkTrigger()
    checkDeactivate()
    flashLed()


"""
alle widgets die ingeladen kunnen worden worden hier gemaakt
"""
w['enterPw'] = Label(master=root, text='Voer het wachtwoord in', height=2)

w['pw'] = Entry(master=root, show="*")

w['speed']=Label(master=root,text='Snelheid')

w['speedScale'] = Scale(master=root, from_=1, to=10,orient=HORIZONTAL)

w['button']=Button(master=root,text='Voer in',command=buttonclick)

w['speedbutton']=Button(master=root,text='Stel in',command=setSpeed)
while True:
    """de mainloop van tkinter"""
        root.update_idletasks()
        root.update()
        main()
