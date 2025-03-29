from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow connections from any device

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("message")
def handle_message(msg):
    print(f"Message received: {msg}")  # Debugging log
    socketio.send(msg, broadcast=True)  # Broadcast message to all connected users

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
