
# Face Detection API

This is a face detection API. The workflow consists of 2 sides, client-side and server-side. 

When the user using the program, the webcam camera receives streaming video data on the client-side, then the video data are sent to the server-side frame by frame. 

The server receives a video frame from the client, then uses that frame as an input of the face detection function to detect faces that appear in the frame. When the computation is done, the server sent the coordinates of all faces that were detected back to the client. 

After the client receives the face coordinates from the server, the client makes a rectangle over face coordinates for showing the detected face region to the user.

## Client-side

On the client-side, the receiving of streaming video data via webcam camera is created by the OpenCV library.

You can run the client follow this command (make sure the server is running)

```bash
python3 client.py
```
## Server-side

The server-side is created by Flask framework and uses the face detection engine as a core algorithm for detecting faces.

For running the server, please use the following command

```bash
python3 server.py
```
