import time
import zmq
import favicon
import requests

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    print(f"Received request: {message}")
    passed_url = str(message)
    url = passed_url[2:]
    url = url[:-1]
    socket.send_string(f"Received request: {url}")

    icons = favicon.get(url)
    icon = icons[0]
    image = requests.get(icon.url)
    image_info = image.content

    print(image_info)

    time.sleep(5)

    socket.send(image_info)


