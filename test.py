from flask import Flask, Response
import cv2
import numpy as np
from PIL import ImageGrab

app = Flask(__name__)

def generate_frames():
    while True:
        # Capture the screen
        printscreen = np.array(ImageGrab.grab(bbox=(0, 40, 1920, 1080)))

        # Convert the image to RGB format
        frame = cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB)

        ret, buffer = cv2.imencode('.png', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
