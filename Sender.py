import zmq
from PIL import Image
from io import BytesIO

context = zmq.Context()

print("Connecting to CS361 socket test server..")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for request in range(1):
    print(f"Sending request {request}")
    socket.send_string("http://www.stackoverflow.com")  # Some website URL.

    message = socket.recv()
    print(f"Received reply {request} [ {message} ]")
    i = Image.open(BytesIO(message))
    i.show()
