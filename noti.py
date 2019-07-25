import requests
from signal import pause
from gpiozero import Button

button = Button(3)
A = "Door Bell"
def hello():
    print("Hello Zion")
    requests.post("https://maker.ifttt.com/trigger/global/with/key/denIvf-6DKIG3yS_Ovo8p4", A)
   
    
    
print("Hello Ghanq")
button.when_pressed =  hello
pause()