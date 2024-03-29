import socket
from time import sleep
import picamera

# Connect a client socket to my_server:8000 (change my_server to the
# hostname of your server)
client_socket = socket.socket()
client_socket.connect(("my_server", 8000))

# Make a file-like object out of the connection
connection = client_socket.makefile("wb")
try:
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 24
    # Start a preview and let the camera warm up for 2 seconds
    camera.start_preview()
    sleep(2)
    # Start recording, sending the output to the connection for 60
    # seconds, then stop
    camera.start_recording(connection, format="h264")
    while True:
        sleep(100)
finally:
    connection.close()
    client_socket.close()
