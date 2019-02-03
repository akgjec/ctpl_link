#!/usr/bin/env python
#
# Project: Video Streaming with Flask
# Author: Log0 <im [dot] ckieric [at] gmail [dot] com>
# Date: 2014/12/21
# Website: http://www.chioka.in/
# Description:
# Modified to support streaming out with webcams, and not just raw JPEGs.
# Most of the code credits to Miguel Grinberg, except that I made a small tweak. Thanks!
# Credits: http://blog.miguelgrinberg.com/post/video-streaming-with-flask
#
# Usage:
# 1. Install Python dependencies: cv2, flask. (wish that pip install works like a charm)
# 2. Run "python main.py".
# 3. Navigate the browser to the local webpage.
from flask import Flask, render_template, Response
from camera import VideoCamera
from time import sleep
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def about():
        return render_template('about.html')

@app.route('/configure')
def index():
    return render_template('')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
def start():
    try:
        app.run(host='thisserveraddress', debug=True)
    except Exception as Err:
        print(Err)
        sleep(0.5)
        start()

def main():
    app.run(host='172.25.10.210', debug=True)

if __name__ == '__main__':
<<<<<<< HEAD
    main()
=======
    start()

>>>>>>> f2fc3523d9e0bbabc9fa9178a6e49d5de6367ded
