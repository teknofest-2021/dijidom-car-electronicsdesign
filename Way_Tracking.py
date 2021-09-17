import RPi.GPIO as GPIO
import time
import Engine


GPIO.setmode(GPIO.BCM)

#GPIO.setwarnings(False)
led_1=13
led_2=26
led_3=25
#led_4=12

GPIO.setup(led_1,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_2,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_3,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

print("Start")

while True:
    input_1 = GPIO.input(led_1)
    input_2 = GPIO.input(led_2)
    input_3 = GPIO.input(led_3)
    #input_4 = GPIO.input(led_4)
    ## True siyah görüyor
    ## False beyaz görüyor
    
    while input_1 == False and input_2 == True and input_3 == False:
        input_1 = GPIO.input(led_1)
        input_2 = GPIO.input(led_2)
        input_3 = GPIO.input(led_3)
        Engine.Forward()
        print("1 False - 2 True - 3 False (İLERİ)")
        
    while input_1 == True and input_2 == True and input_3 == False:
        input_1 = GPIO.input(led_1)
        input_2 = GPIO.input(led_2)
        input_3 = GPIO.input(led_3)
        Engine.Left()
        print("1 True - 2 True - 3 False (SOLA)")
        #if input_1 == False or input_2 == True:
         #   break
    while input_1 == False and input_2 == True and input_3 == True:
        input_1 = GPIO.input(led_1)
        input_2 = GPIO.input(led_2)
        input_3 = GPIO.input(led_3)
        Engine.Right()
        print("1 False - 2 True - 3 True (SAĞA)")
    
    while input_1 == False and input_2 == False and input_3 == False:
        input_1 = GPIO.input(led_1)
        input_2 = GPIO.input(led_2)
        input_3 = GPIO.input(led_3)
        Engine.stop()
        print("1 False - 2 False - 3 False (DURDU)")
        break
    while input_1 == True and input_2 == True and input_3 == True:
        input_1 = GPIO.input(led_1)
        input_2 = GPIO.input(led_2)
        input_3 = GPIO.input(led_3)
        Engine.stop()
        print("1 False - 2 False - 3 False (DURDU)")
        break
    
    time.sleep(0.1)
    
GPIO.cleanup()