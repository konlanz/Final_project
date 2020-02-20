from flask import Flask, render_template
from flask import request
import requests
from flask_socketio import SocketIO, emit
from gpiozero import LED, Button
import RPi.GPIO as GPIO
from datetime import datetime
from signal import pause
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.LOW)
led = LED(4)
ledy = LED(22)
ledb = LED(26)
button = Button(2)
buttonx = Button(3)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
@app.route('/home')
def index():
    return render_template('index.html')
@socketio.on('connect')
def on_connect():
    emit('after connect',  "hello connected")

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
@socketio.on('hello')
def handle_message(message):
    global start, stop
    
    if(message == 1 ):
        GPIO.output(17, GPIO.LOW)
        start = datetime.now()
    else:
        GPIO.output(17, GPIO.HIGH)
        
    
    stop = datetime.now()
    timmerx = stop-start
    socketio.emit('timmer', str(timmerx))


@socketio.on('blueled')
def handle_message(message):
    global start, stop
    
    if(message == 1 ):
        ledb.on()
        start = datetime.now()
    else:
        ledb.off()
        
    
    stop = datetime.now()
    timmerx = stop-start
    socketio.emit('timmerb', str(timmerx))
    
    
@socketio.on('yeled')
def handle_message(message):
    global start, stop
    
    if(message == 1 ):
        ledy.on()
        start = datetime.now()
    else:
        ledy.off()
        
    
    stop = datetime.now()
    timmerx = stop-start
    socketio.emit('timmery', str(timmerx))

light_on = False

def handle_abc():
    global start, stop 
    global light_on
    if(light_on):
        led.off()
        light_on = False
        socketio.emit('button', 0)
            
    else:
        led.on()
        light_on = True
        socketio.emit('button', 1)
        start = datetime.now()
        
    stop = datetime.now()
    timmerx = stop-start
    print(str(timmerx))
    socketio.emit('timmer', str(timmerx))
 
    
button.when_pressed = handle_abc
A = "Door Bell"
def hello():
    print("Hello Zion")
    requests.post("https://maker.ifttt.com/trigger/global/with/key/denIvf-6DKIG3yS_Ovo8p4", A)
   
    

buttonx.when_pressed =  hello

                
@app.route('/login')
def login():
    return render_template('index.html')
@app.route('/signup')
def signup():
    return render_template('index.html')

@app.route('/')
def home():
    return render_template('xindex.html')
if __name__ == '__main__':
    socketio.run(app)
