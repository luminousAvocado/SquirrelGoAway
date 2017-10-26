# import modules
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)             # Sets pin 3 as green LED output pin
GPIO.setup(5, GPIO.OUT)             # Sets pin 5 as red LED output pin
GPIO.setup(11, GPIO.IN)             # Reads input from the PIR sensor on pin 11



def blink(pin):
    GPIO.output(pin,GPIO.HIGH)  
    time.sleep(0.1)  
    GPIO.output(pin,GPIO.LOW)  
    time.sleep(0.1)  
    return


while True:
  i=GPIO.input(11)                  # Reads input from pin 11 and sets to 'i'
  if i==0:                          # When input from pin 11(PIR sensor) is 0/GPIO.LOW/False (not sensing anything)
        GPIO.output(3, 1)           # Turn green LED pin 3 ON
        GPIO.output(5, 0)           # Turn red LED pin 5 OFF
        print ("No intruders")
        time.sleep(0.5)
  elif i==1:                        # When input from the PIR sensor is 1/GPIO.HIGH/True (detecting motion)
        GPIO.output(3, 0)           # Turn green LED pin 3 OFF
        blink(5)                    # Turn red LED pin 5 ON
        print ("Intruder detected!")
        time.sleep(0.5)