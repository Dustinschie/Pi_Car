import RPi.GPIO as gpio
import time
import os
import sys
import picamera
import cv2
import io
import numpy as np


class Car(object):
    __directions = {
        'w':[0,0], 
        's':[1,1], 
        'a':[1,0], 
        'd':[0,1], 
        'wd':[0,2],
        'dw':[0,2],
        'wa':[2,0],
        'aw':[2,0],
        'sa':[2,1],
        'as':[2,1],
        'ds':[1,2],
        'sd':[1,2]}


    def __init__(self, motor1A = 7, motor1B = 11, 
                        motor2A = 13, motor2B = 15):
        self.motor1A = motor1A
        self.motor1B = motor1B
        self.motor2A = motor2A
        self.motor2B = motor2B
        self.isCameraOn = False
        self.initMotors()
        # self.initCamera()

    def __del__(self):
        print("Cleaning-up motors\n")
        gpio.cleanup()
        if self.isCameraOn:
            print("Closing cameras")
            picamera.PiCamera().close()

    def initMotors(self):
        gpio.cleanup()
        gpio.setmode(gpio.BOARD)
        print("intiating Motors: \
            \n\tLeft Motors pins: " + str(self.motor1A) + " , " + str(self.motor1B)
            + "\n\tRight Motors pins: " + str(self.motor2A) + " , " + str(self.motor2B) 
            + "\n")

        gpio.setup(self.motor1A, gpio.OUT)
        gpio.setup(self.motor1B, gpio.OUT)
        gpio.setup(self.motor2A, gpio.OUT)
        gpio.setup(self.motor2B, gpio.OUT)

    def initCamera(self, resolution = (640, 480)):
        print("Initiating Camera with resolution: " + str(resolution))
        picamera.PiCamera().resolution = resolution
        time.sleep(0.2)
        self.isCameraOn = True

    # directions 0: forward
    #            1: reverse
    #            x: nothing
    def rightMotor(self, direction = 2):
        if direction is 0:
            gpio.output(self.motor1A, True)
            gpio.output(self.motor1B, False)
        elif direction is 1:
            gpio.output(self.motor1A, False)
            gpio.output(self.motor1B, True)
        else:
            gpio.output(self.motor1A, False)
            gpio.output(self.motor1B, False)


    def leftMotor(self, direction = 2):
        if direction is 0:
            gpio.output(self.motor2A, False)
            gpio.output(self.motor2B, True)
        elif direction is 1:
            gpio.output(self.motor2A, True)
            gpio.output(self.motor2B, False)
        else:
            gpio.output(self.motor2A, False)
            gpio.output(self.motor2B, False)


    # input     w:  forward
    #           a:  counterclockwise
    #           s:  clockwise
    #           d:  reverse
    #           wa: left forward
    #           wd: right forward
    #           aw: left forward
    #           dw: right forward
    #           sa: left reverse
    #           sd: right reverse
    #           as: left reverse
    #           ds: right reverse

    # duration  numbers of seconds the motors are on
    def move(self, input = '', duration = 0.2):
        if len(input) != 0 and input in Car.__directions:
            control = Car.__directions[input]
            self.leftMotor(control[1])
            self.rightMotor(control[0])

            time.sleep(0.2)

            self.leftMotor()
            self.rightMotor()

    #   returns an OpenCV image object
    def camCaptureImage(self):
        stream = io.BytesIO()
        picamera.PiCamera().capture(stream, format='jpeg')
        data = np.fromstring(stream.getvalue(), dtype=np.uint8)
        return cv2.imdecode(data, 1)

    def camCaptureVideo(self):
        stream = io.BytesIO()
        with picamera.PiCamera() as camera:
            camera.resolution = (640, 480)
            camera.start_recording(stream, quantization=23)
            camera.wait_recording(15)
            camera.stop_recording()