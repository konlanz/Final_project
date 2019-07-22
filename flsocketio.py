from flask import Flask, render_template
from flask import request
from flask_socketio import SocketIO, emit
from gpiozero import LED
led = LED(17)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
@app.route('/')
def index():
    return render_template('index.html')
@socketio.on('connect')
def on_connect():
    emit('after connect',  {'data':'hello worl'})


@socketio.on('hello')
def handle_message(message):
    print(message)
    if(message == 1):
        led.on()
    else:
        led.off()
@app.route('/whereami')
def whereami():
    return 'Ghana'
if __name__ == '__main__':
    socketio.run(app)