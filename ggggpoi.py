import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
#GPIO.setup(12,GPIO.OUT) ## Saida 1
#GPIO.setup(16,GPIO.OUT) ## Saida 2
GPIO.setup(15,GPIO.OUT) ## Saida 3
#GPIO.setup(13,GPIO.OUT) ## Saida 4
GPIO.setwarnings(False)

for i in range(0,50):
##    GPIO.output(12,1)
##    time.sleep(1)
##    GPIO.output(16,1)
##    time.sleep(1)
##    GPIO.output(11,1)
##    time.sleep(1)
##    GPIO.output(13,1)
##    time.sleep(1)
##    
##    GPIO.output(12,0)
##    time.sleep(1)
##    GPIO.output(16,0)
##    time.sleep(1)
##    GPIO.output(11,0)
##    time.sleep(1)
##    GPIO.output(13,0)
##    time.sleep(1)

    GPIO.output(15,1)
    time.sleep(1)
    
    GPIO.output(15,0)
    time.sleep(1)
GPIO.cleanup()


    
