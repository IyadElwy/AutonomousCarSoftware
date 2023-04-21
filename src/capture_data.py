from bottle import route, run, template, request

import threading
from time import sleep
from csv import writer
from PIL import Image
import os

from picamera import PiCamera
from picamera.array import PiRGBArray

from MotorControl.motor_controller import MotorDriver

###############################################

f_b_motor = MotorDriver(25, 23, 24)
l_r_motor = MotorDriver(16, 20, 21)

f_b_speed = 60
l_r_speed = 100

###############################################

camera = PiCamera()
camera.resolution = (640, 480)

raw_capture = PiRGBArray(camera, size=(640, 480))

sleep(0.3)

###############################################

steering_data = [0, 0, 0, 0]  # f, b, r, l

###############################################

modes = {0: 'DRIVING', 1: 'TRAINING', 2: 'AI'}
current_mode = modes[0]

###############################################


@route('/')
def index():
    cmd = request.GET.get('command', '')

    if cmd == 'f':
        f_b_motor.forward(f_b_speed, 0)
        steering_data[0] = 1

    elif cmd == 'b':
        f_b_motor.backward(f_b_speed, 0)
        steering_data[1] = 1

    elif cmd == 'r':
        l_r_motor.forward(l_r_speed, 0)
        steering_data[2] = 1

    elif cmd == 'l':
        l_r_motor.backward(l_r_speed, 0)
        steering_data[3] = 1

    elif cmd == 's_fb':
        f_b_motor.stop(0)
        steering_data[0] = 0
        steering_data[1] = 0

    elif cmd == 's_lr':
        l_r_motor.stop(0)
        steering_data[2] = 0
        steering_data[3] = 0

    elif cmd == 'change_mode':
        steering_data[0] = 1
        l_r_motor.stop(0)
        f_b_motor.stop(0)

        # if current_mode == 'DRIVING':
        #     current_mode = modes[1]
        # elif current_mode == 'TRAINING':
        #     current_mode == modes[2]
        # elif current_mode == 'AI':
        #     current_mode == modes[0]

    return template('home.tpl')


#########################################################

def get_new_directory_name():
    if not os.path.isdir('../data'):
        return '../data/t1'
    else:
        subfolders = [f.path for f in os.scandir('../data') if f.is_dir()]
        print(subfolders)


def capture_data():
    get_new_directory_name()
    if current_mode == 'TRAINING':
        for i, frame in enumerate(camera.capture_continuous(raw_capture, format='rgb', use_video_port=True)):
            image = frame.array

            r = [*steering_data, f'../data/t1/{i}.jpg']

            img = Image.fromarray(image, "RGB")
            img.save(f'../data/t1/{i}.jpg')

            with open('../data/t1/steering.csv', 'a+') as f:
                writer_object = writer(f)
                writer_object.writerow(r)

            raw_capture.truncate(0)

        camera.close()


#########################################################
if __name__ == '__main__':
    t1 = threading.Thread(target=run, kwargs=dict(host='0.0.0.0', port=80))
    t2 = threading.Thread(target=capture_data)
    t1.start()
    t2.start()
