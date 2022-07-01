from time import sleep
import pigpio
import subprocess


def RGB_test():
    print("***[hardware RGB_test]***")
    pi = pigpio.pi()
    brightness = 0
    cycle_time = 0.01
    pause_time = 2

    subprocess.call(['sudo pigpiod'], shell=True)
    while(brightness < 255):
        brightness = brightness+1;
        pi.set_PWM_dutycycle(18, brightness)
        sleep(cycle_time)

    while(brightness > 0):
        brightness=brightness-1;
        pi.set_PWM_dutycycle(18, brightness)
        sleep(cycle_time)
        
    sleep(pause_time)
        
    while(brightness < 255):
        brightness=brightness+1;
        pi.set_PWM_dutycycle(23, brightness)
        sleep(cycle_time)

    while(brightness > 0):
        brightness=brightness-1;
        pi.set_PWM_dutycycle(23, brightness)
        sleep(cycle_time)
        
    sleep(pause_time)
        
    while(brightness < 255):
        brightness=brightness+1;
        pi.set_PWM_dutycycle(24, brightness)
        sleep(cycle_time)
        
    while(brightness > 0):
        brightness=brightness-1;
        pi.set_PWM_dutycycle(24, brightness)
        sleep(cycle_time)
        
    pi.stop()	
    return
