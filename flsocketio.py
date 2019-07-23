from flask import Flask, render_template
from flask import request
from flask_socketio import SocketIO, emit
from gpiozero import LED, Button
from signal import pause
led = LED(17)
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
    print("Hello console")
    
    if button.is_pressed:
        print("Hello world")
    else:
        print("Hello GHANA")

print("Hello world")


@socketio.on('hello')
def handle_message(message):
    if(message == 1 ):
        led.on()        
    else:
        led.off()
        


light_on = False
def handle_abc():
    global light_on
    if(light_on):
        led.off()
        light_on = False
        socketio.emit('button', 0)
    else:
        led.on()
        light_on = True
        socketio.emit('button', 1)
    


button.when_pressed = handle_abc

    

              
@app.route('/whereami')
def whereami():
    return 'Ghana'
if __name__ == '__main__':
    socketio.run(app)