from project import app, socketio


if __name__ == "__main__":
    port = 5001
    print(f"Smartphone Running in {port}")
    socketio.run(app, port=port)
