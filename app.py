from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import random
import datetime

app = Flask(__name__)
socketio = SocketIO(app)

users = []

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("connect")
def handle_connect():
    users.append(request.sid)
    if len(users) >= 2:  # If at least 2 users are online
        user1, user2 = users[:2]
        emit("message", {"message": "You have been connected to a stranger!", "timestamp": get_time()}, room=user1)
        emit("message", {"message": "You have been connected to a stranger!", "timestamp": get_time()}, room=user2)
        users.remove(user1)
        users.remove(user2)

@socketio.on("message")
def handle_message(msg):
    timestamp = get_time()
    emit("message", {"message": msg, "timestamp": timestamp}, broadcast=True)  # Sends to all users

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")  # Format HH:MM:SS

if __name__ == "__main__":
    socketio.run(app, debug=True)
