from time import sleep

def armMotor(control):

    control.setMotor(-1)
    
    print("Plug in battery!")
    
    for i in range(10):
        control.setRGB(0,0,255)
        print(8-i)
        sleep(0.5)
        control.setRGB(0,0,0)
        sleep(0.5)

    control.setMotor(-0.6)
    sleep(1)
    control.setMotor(-1)
