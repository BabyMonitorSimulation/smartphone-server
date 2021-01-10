from project import app, socketio


if __name__ == "__main__":
    print("Smartphone Running")
    socketio.run(app, port=5001)
