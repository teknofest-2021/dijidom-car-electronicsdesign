import cv2
import Engine as eng
import RPi.GPIO as GPIO
import time

servo2 = 8
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo2,GPIO.OUT, initial=False)
horizontal=GPIO.PWM(servo2,50)

def Rotate_horizontal(d):
    horizontal.start(0)
    horizontal.ChangeDutyCycle(d)
    time.sleep(0.2)
    horizontal.stop()

sayac=0
kamera=cv2.VideoCapture(0)
kamera.set(3,640)
kamera.set(4,480)
while kamera.isOpened():
    ret,kare=kamera.read()
    if ret== True:
        cv2.imshow("resim",kare)
        basilanTus=cv2.waitKey(1)&0xFF
        if basilanTus==ord('r'):
            cv2.imwrite("resim"+str(sayac)+".jpg",kare)
            sayac+=1
        if basilanTus==ord('a'):
            horizontal.start(0)
            horizontal.ChangeDutyCycle(1)
            time.sleep(5)
            horizontal.ChangeDutyCycle(5)
            time.sleep(5)
            horizontal.ChangeDutyCycle(11)
            time.sleep(5)
            horizontal.stop()
        
        if basilanTus==ord('q'):
            GPIO.cleanup()
            break
 
cv2.destroyAllWindows();
exit()