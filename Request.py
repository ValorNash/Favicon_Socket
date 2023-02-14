import zmq
from PIL import Image
from io import BytesIO

context = zmq.Context()

print("Connecting to CS361 socket test server..")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for request in range(1):
    url = "http://www.stackoverflow.com"
    print(f"Sending request: {url}")
    socket.send_string(url)

    message = socket.recv()
    print(f"Received favicon information.")
    i = Image.open(BytesIO(message))
    i.show()
