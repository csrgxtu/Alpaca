from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return 'mrmaster'

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    send(message)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=9100)
