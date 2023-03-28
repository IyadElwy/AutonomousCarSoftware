from bottle import route, run, template, request
from motor_controller import MotorDriver

f_b_motor = MotorDriver(25, 23, 24)
l_r_motor = MotorDriver(16, 20, 21)

f_b_speed = 60
l_r_speed = 100

@route('/')
def index():
    cmd = request.GET.get('command', '')
    
    if cmd == 'f':
        f_b_motor.forward(f_b_speed, 0)
        
    elif cmd == 'b':
        f_b_motor.backward(f_b_speed, 0)
        
    elif cmd == 'r':
        l_r_motor.forward(f_b_speed, 0)
        
            
    elif cmd == 'l':
        l_r_motor.backward(f_b_speed, 0)
        
                    
    elif cmd == 's_fb':
        f_b_motor.stop(0)

    elif cmd == 's_lr':
        l_r_motor.stop(0)

    return template('home.tpl')



if __name__ == '__main__':
    run(host='0.0.0.0', port=80)

