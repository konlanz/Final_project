from flask import Flask, render_template
from flask import request
from flask_socketio import SocketIO, emit
from gpiozero import LED, Button
from datetime import datetime
from signal import pause
led = LED(17)
ledy = LED(22)
ledb = LED(26)
button = Button(2)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
@app.route('/')
def index():
    return render_template('index.html')
@socketio.on('connect')
def on_connect():
    emit('after connect',  "hello connected")


@socketio.on('hello')
def handle_message(message):
    global start, stop
    
    if(message == 1 ):
        led.on()
        start = datetime.now()
    else:
        led.off()
        
    
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

    

              
@app.route('/whereami')
def whereami():
    return 'Ghana'
if __name__ == '__main__':
    socketio.run(app)