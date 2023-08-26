from machine import Pin,ADC,PWM
class IRArray():
    sensorPins = []
    output = []
    
    def __init__(self,*pins):
        i = 0
        print(pins)
        for pin in pins:
            self.sensorPins.append(ADC(Pin(pin)))
            self.sensorPins[i].atten(ADC.ATTN_11DB)
            i +=1
        
    def sensorReading(self,sensor):
        return (sensor.read() > 1700)
    
    def irArrayOutput(self):
        self.output = []
        for sensor in self.sensorPins:
            self.output.append(self.sensorReading(sensor))    
        return self.output
            
