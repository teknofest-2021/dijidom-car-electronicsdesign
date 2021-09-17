import RPi.GPIO as GPIO          
import time
import cv2

Bin1 = 22
Bin2 = 16
Bin3 = 5
Bin4 = 6
Fin1 = 23
Fin2 = 24
Fin3 = 17
Fin4 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(Bin1,GPIO.OUT)
GPIO.setup(Bin2,GPIO.OUT)
GPIO.setup(Bin3,GPIO.OUT)
GPIO.setup(Bin4,GPIO.OUT)
GPIO.setup(Fin1,GPIO.OUT)
GPIO.setup(Fin2,GPIO.OUT)
GPIO.setup(Fin3,GPIO.OUT)
GPIO.setup(Fin4,GPIO.OUT)




def l_back_forward():
    GPIO.output(Bin1,GPIO.HIGH)
    GPIO.output(Bin2,GPIO.LOW)
def l_back_backward():
    GPIO.output(Bin1,GPIO.LOW)
    GPIO.output(Bin2,GPIO.HIGH)
def r_back_forward():
    GPIO.output(Bin3,GPIO.HIGH)
    GPIO.output(Bin4,GPIO.LOW)
def r_back_backward():
    GPIO.output(Bin3,GPIO.LOW)
    GPIO.output(Bin4,GPIO.HIGH)

def r_front_backward():
    GPIO.output(Fin1,GPIO.HIGH)
    GPIO.output(Fin2,GPIO.LOW)
def r_front_forward():
    GPIO.output(Fin1,GPIO.LOW)
    GPIO.output(Fin2,GPIO.HIGH)
def l_front_forward():
    GPIO.output(Fin3,GPIO.LOW)
    GPIO.output(Fin4,GPIO.HIGH)
def l_front_backward():
    GPIO.output(Fin3,GPIO.HIGH)
    GPIO.output(Fin4,GPIO.LOW)
def Forward():
    l_front_forward()
    r_front_forward()
    l_back_forward()
    r_back_forward()
def Backward():
    l_front_backward()
    r_front_backward()
    l_back_backward()
    r_back_backward()
def stop():
    GPIO.output(Bin1,GPIO.LOW)
    GPIO.output(Bin2,GPIO.LOW)
    GPIO.output(Bin3,GPIO.LOW)
    GPIO.output(Bin4,GPIO.LOW)
    GPIO.output(Fin1,GPIO.LOW)
    GPIO.output(Fin2,GPIO.LOW)
    GPIO.output(Fin3,GPIO.LOW)
    GPIO.output(Fin4,GPIO.LOW)

def Left():
    r_front_forward()
    r_back_forward()
    l_front_backward()
    l_back_backward()
def Right():
    r_front_backward()
    r_back_backward()
    l_front_forward()
    l_back_forward()

