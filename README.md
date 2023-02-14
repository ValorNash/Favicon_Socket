# Favicon_Socket
A socket program using ZeroMQ that receives a website URL, and returns data of the favicon that can be reconstructed into an image. 

*OVERVIEW OF SERVICE FUNCTION*

To use this service, the Sender (see example "Sender.py" file) must first send a valid website url in the form of a string and formatted correctly, 
such as "http://www.stackoverflow.com" or "https://www.github.com". The service will then respond with the raw image data for the favicon of the 
url requested. If no favicon is found, the service will instead return the error message "No favicon could be found for url {url}". 

In order to use this microservice, you will need ZeroMQ.

 *REQUEST EXAMPLE*
 
To request information from the microservice, you will need to send the url string using ZeroMQ and on the local port 5555. An example of the request
can be seen below. This example also handles the error messages by converting the incoming message to a string, and then determining if the string is 
the error.

Please note that the example using pillow (formerly PIL) to convert the raw image data into an image which it then opens. 
 
![image](https://user-images.githubusercontent.com/86168279/218640555-0688ef88-7062-4019-8437-49e0bd864508.png)
