from flask import Flask, render_template, Response
import cv2
import numpy as np

app = Flask(__name__)

# Function to track tennis balls
def track_ball():
    cap = cv2.VideoCapture(0)  # Open the camera

    while True:
        ret, frame = cap.read()  # Read a frame from the camera
        if not ret:
            break

        # Your ball tracking code here...

        # Encode frame to JPEG
        ret, jpeg = cv2.imencode('.jpg', frame)
        frame = jpeg.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(track_ball(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
