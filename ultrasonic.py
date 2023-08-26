import machine, time
from machine import Pin


class HCSR04:
   
    # echo_timeout_us is based in chip range limit (400cm)
    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=500*2*30):

        self.echo_timeout_us = echo_timeout_us
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin

    def send_pulse_and_wait(self):
        self.trigger = Pin(self.trigger_pin, mode=Pin.OUT, pull=None)
        self.trigger.value(0)
        time.sleep_us(10)
        self.trigger.value(1)
        time.sleep_us(10)
        self.trigger.value(0)
        self.echo = Pin(self.echo_pin, mode=Pin.IN, pull=None)
        try:
            pulse_time = machine.time_pulse_us(self.echo, 1, self.echo_timeout_us)
            print(pulse_time)
            return pulse_time
        except :
            exit()
        finally :
            self.echo = None 


    def distance_cm(self):
        
        pulse_time = self.send_pulse_and_wait()
        cms = (pulse_time / 2) / 29.1
        return cms
    
    


