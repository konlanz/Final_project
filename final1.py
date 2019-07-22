from gpiozero import LED
from time import sleep
from flask import Flask, render_template, request

led = LED(17)
app = Flask(__name__)
@app.route('/')
def index():
    ledx = "on"
    if (ledx == "on"):
        led.on()
    return "hello world"    
        

@app.route('/whereami')
def whereami():
    ledx = "off"
    if (ledx == "off"):
        led.off()
    return "hello world" 
    return 'Ghana'

if __name__ == '__main__':
    app.run(debug=True, host= '0.0.0.0')

