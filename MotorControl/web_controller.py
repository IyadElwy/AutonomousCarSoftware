from bottle import route, run, template, request
from motor_controller import MotorDriver

f_b_motor = MotorDriver(25, 23, 24)
l_r_motor = MotorDriver(21, 20, 16)


@route('/')
def index():
    cmd = request.GET.get('command', '')
    if cmd == 'f':
        f_b_motor.forward(100, 0)
    elif cmd == 'b':
        f_b_motor.backward(100, 0)
    elif cmd == 'l':
        l_r_motor.forward(100, 0)
    elif cmd == 'r':
        l_r_motor.backward(100, 0)
    elif cmd == 's':
        f_b_motor.stop(1)
        l_r_motor.stop(1)
        
    return template('home.tpl')


 
if __name__ == '__main__':
    run(host='0.0.0.0', port=80)

