from machine import Pin,ADC,PWM
from time import sleep

from robotController import Robot
from irSensors import IRArray

irarray = IRArray(13,4,26,14,32)

robot = Robot()
while True:
    output = irarray.irArrayOutput()
    print(output)
    robot.stopForwardLeft()
    robot.stopForwardRight()
    if(output[4]):
        while not (output[2]):
            robot.driveForwardLeft(600)
            output = irarray.irArrayOutput()
        robot.stopForwardLeft()
    elif (output[0]):
        while not (output[2]):
            robot.driveForwardRight(600)
            output = irarray.irArrayOutput()
        robot.stopForwardRight()
    else :
        robot.driveForwardLeft(600)
        robot.driveForwardRight(600)
    sleep(0.1)
        
        


