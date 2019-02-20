import RPi.GPIO as GPIO
import picamera
import time as iceT
from pygame import *
import PestSound
import pygame
import sys


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)

class motionDetect:
    
    def start(sounds):
        try:
            timer = True
            if sounds == None:
                squirrels = PestSound.s_dict()
            else:
                squirrels = sounds
            print ("Initiating Squirrel Deterrence Protocol")
            p = GPIO.PWM(7,50)
            p.start(7.5)
            camera = picamera.PiCamera()
            camera.iso = 800
            #camera.resolution = (800, 450)
            #camera.start_preview()
            iceT.sleep(1)
            while timer:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            sys.exit()
                i = GPIO.input(11)
                if i==0:
                    print ("No intruders")
                    GPIO.output(3,0)
                    GPIO.output(5,0)
                    iceT.sleep(0.1)
                elif i==1:
                    camera.capture("PERPS/" + iceT.strftime("%y%m%d_%H-%M-%S") + ".jpg")
                    p.ChangeDutyCycle(12.5)
                    iceT.sleep(0.5)
                    p.ChangeDutyCycle(2.5)
                    print ("INTRUDER")
                    GPIO.output(3,1)
                    GPIO.output(5,1)
                    iceT.sleep(0.1)
                    GPIO.output(3,0)
                    GPIO.output(5,0)
                    iceT.sleep(0.1)
                    # Sound Test
                    #squirrels = PestSound.s_dict()
                    squirrels.get_files()
                    squirrels.play_rand_file()
        except KeyboardInterrupt:
            print ("Quitting")
            GPIO.cleanup()