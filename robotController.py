from machine import Pin,ADC,PWM
class Robot():
    forwardLeftPin = 17
    backwardLeftPin = 16
    forwardRightPin = 18
    backwardRightPin = 27
    frequency = 1000
    
    def __init__(self):
        self.forwardleft = PWM(Pin(self.forwardLeftPin,Pin.OUT),freq = self.frequency)
        self.backwardLeft = PWM(Pin(self.backwardLeftPin,Pin.OUT),freq= self.frequency)
        self.forwardRight = PWM(Pin(self.forwardRightPin,Pin.OUT),freq=self.frequency)
        self.backwardRight = PWM(Pin(self.backwardRightPin,Pin.OUT),freq=self.frequency)
        
    def driveForwardLeft(self,speed):
        self.forwardleft.duty(speed)
        self.backwardLeft.duty(0)
        
    def driveForwardRight(self,speed):
        self.forwardRight.duty(speed)
        self.backwardRight.duty(0)
        
    def stopForwardLeft(self):
        self.forwardleft.duty(0)
        self.backwardLeft.duty(0)
    def stopForwardRight(self):
        self.forwardRight.duty(0)
        self.backwardRight.duty(0)
      
