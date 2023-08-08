import RPi.GPIO as GPIO
import time
import socket
import random
import subprocess


TCP_IP = '192.168.254.11'
TCP_PORT = 5612
BUFFER_SIZE = 1024 
MESSAGE = b"Play"
MESSAGE1 = b"Extra"
MESSAGE2 = b"0"

MESSAGE3 = b"Safe"
MESSAGE8 = b"Freddy wrong"
MESSAGE9 = b"1"
MESSAGE10 = b"2"
MESSAGE11 = b"3"
MESSAGE12 = b"4"
MESSAGE13 = b"5"
MESSAGE14 = b"6"
MESSAGE15 = b"Start"
MESSAGE16 = b"Congrats"





GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_TRIGGER = 20
GPIO_ECHO = 21
GPIO_TRIGGER1 = 26
GPIO_ECHO1 = 19
GPIO_TRIGGER2 = 27
GPIO_ECHO2 = 22




GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)
GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)




s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)	
GPIO.setup(24,GPIO.IN)
GPIO.setup(16,GPIO.IN)
GPIO.setup(17,GPIO.IN)

def distance():

    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def distance1():

    GPIO.output(GPIO_TRIGGER1, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER1, False)
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(GPIO_ECHO1) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO1) == 1:
        StopTime = time.time()
    TimeElapsed = StopTime - StartTime
    distance1 = (TimeElapsed * 34300) / 2
 
    return distance1

def distance2():

    GPIO.output(GPIO_TRIGGER2, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER2, False)
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(GPIO_ECHO2) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO2) == 1:
        StopTime = time.time()
    TimeElapsed = StopTime - StartTime
    distance2 = (TimeElapsed * 34300) / 2
 
    return distance2

count = 0

while True:
    
    
    
    if GPIO.input(24):
        count = 0
        print(count)
        s.send(MESSAGE)
        subprocess.run(["python","Seq1.py"])
        #data=s.recv(BUFFER_SIZE)
        time.sleep(1)
        s.send(MESSAGE2)
        #data=s.recv(BUFFER_SIZE)
        time.sleep(1)
    
        
    elif GPIO.input(16):
        s.send(MESSAGE1)        #data=s.recv(BUFFER_SIZE)
        time.sleep(1)
        s.send(MESSAGE2)
        time.sleep(1)
        
    elif GPIO.input(17):
        s.send(MESSAGE15)
        subprocess.run(["python","Seq1.py"])
        time.sleep(1)
        subprocess.run(["python","Seq1.py"])
        s.send(MESSAGE2)
        
    
    
               
          
        
    elif __name__ == '__main__':
        try:
                dist = distance()
                dist1 = distance1()
                dist2 = distance2()
                if dist  >= 1 and dist <= 10:
                    count = count + 1
                    print (count)
                    if count == 1:
                        print ("Measured Distance = %.1f cm" % dist)
                        s.send(MESSAGE3)
                        subprocess.run(["python","Seq2.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq2.py"])
                        s.send(MESSAGE2)
                        time.sleep(3.5)
                        subprocess.run(["python","Seq3.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq3.py"])
                        
                    elif count == 2:
                        print ("Measured Distance = %.1f cm" % dist)
                        s.send(MESSAGE3)
                        subprocess.run(["python","Seq2.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq2.py"])
                        s.send(MESSAGE2)
                        time.sleep(3.5)
                        subprocess.run(["python","Seq3.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq3.py"])
                    
                    elif count == 3:
                        print ("Measured Distance = %.1f cm" % dist)
                        s.send(MESSAGE3)
                        subprocess.run(["python","Seq2.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq2.py"])
                        s.send(MESSAGE2)
                        time.sleep(3.5)
                        subprocess.run(["python","Seq3.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq3.py"])
                        
                    
                     
                    elif count == 4:
                        print("gg")
                        s.send(MESSAGE16)
                        subprocess.run(["python","Seq2.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq2.py"])
                        s.send(MESSAGE2)
                        time.sleep(6.5)
                        subprocess.run(["python","Seq3.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq3.py"])
                    
                elif dist >= 18  and dist <= 25:
                    count = count + 1
                    print (count)
                    print ("hi")
                    if count == 1:
                        print ("Measured Distance = %.1f cm" % dist)
                        s.send(MESSAGE3)
                        subprocess.run(["python","Seq2.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq2.py"])
                        s.send(MESSAGE2)
                        time.sleep(3.5)
                        subprocess.run(["python","Seq3.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq3.py"])
                        
                    elif count == 2:
                        print ("Measured Distance = %.1f cm" % dist)
                        s.send(MESSAGE3)
                        subprocess.run(["python","Seq2.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq2.py"])
                        s.send(MESSAGE2)
                        time.sleep(3.5)
                        subprocess.run(["python","Seq3.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq3.py"])
                    
                    elif count == 3:
                        print ("Measured Distance = %.1f cm" % dist)
                        s.send(MESSAGE3)
                        subprocess.run(["python","Seq2.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq2.py"])
                        s.send(MESSAGE2)
                        time.sleep(3.5)
                        subprocess.run(["python","Seq3.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq3.py"])
                    
                     
                    elif count == 4:
                        print("gg")
                        s.send(MESSAGE16)
                        subprocess.run(["python","Seq2.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq2.py"])
                        s.send(MESSAGE2)
                        time.sleep(6.5)
                        subprocess.run(["python","Seq3.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq3.py"])
                        
                        
                    
              
                    
                elif dist1  >= 1 and dist1 <= 10:
                    count = count + 1
                    print (count)
                    if count == 1:
                        print ("Measured Distance = %.1f cm" % dist1)
                        s.send(MESSAGE3)
                        subprocess.run(["python","Seq2.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq2.py"])
                        s.send(MESSAGE2)
                        time.sleep(3.5)
                        subprocess.run(["python","Seq3.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq3.py"])
                        
                    
                    elif count == 2:
                        print ("Measured Distance = %.1f cm" % dist1)
                        s.send(MESSAGE3)
                        subprocess.run(["python","Seq2.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq2.py"])
                        s.send(MESSAGE2)
                        time.sleep(3.5)
                        subprocess.run(["python","Seq3.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq3.py"])
                    
                    elif count == 3:
                        print ("Measured Distance = %.1f cm" % dist1)
                        s.send(MESSAGE3)
                        subprocess.run(["python","Seq2.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq2.py"])
                        s.send(MESSAGE2)
                        time.sleep(3.5)
                        subprocess.run(["python","Seq3.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq3.py"])
                    
                     
                    elif count == 4:
                        print("gg")
                        s.send(MESSAGE16)
                        subprocess.run(["python","Seq2.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq2.py"])
                        s.send(MESSAGE2)
                        time.sleep(6.5)
                        subprocess.run(["python","Seq3.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq3.py"])
                        
                        
                    
                    
                elif dist1  >= 18 and dist1 <= 25:
                    count = count + 1
                    print (count)
                    if count == 1:
                        print ("Measured Distance = %.1f cm" % dist1)
                        s.send(MESSAGE3)
                        subprocess.run(["python","Seq2.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq2.py"])
                        s.send(MESSAGE2)
                        time.sleep(3.5)
                        subprocess.run(["python","Seq3.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq3.py"])
                    
                    elif count == 2:
                        print ("Measured Distance = %.1f cm" % dist1)
                        s.send(MESSAGE3)
                        subprocess.run(["python","Seq2.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq2.py"])
                        s.send(MESSAGE2)
                        time.sleep(3.5)
                        subprocess.run(["python","Seq3.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq3.py"])
                        
                    elif count == 3:
                        print ("Measured Distance = %.1f cm" % dist1)
                        s.send(MESSAGE3)
                        subprocess.run(["python","Seq2.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq2.py"])
                        s.send(MESSAGE2)
                        time.sleep(3.5)
                        subprocess.run(["python","Seq3.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq3.py"])
                    
                     
                    elif count == 4:
                        print("gg")
                        s.send(MESSAGE16)
                        subprocess.run(["python","Seq2.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq2.py"])
                        s.send(MESSAGE2)
                        time.sleep(6.5)
                        subprocess.run(["python","Seq3.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq3.py"])
                        
                        
                    
                    
                elif dist2 >= 1 and dist2 <= 10:
                    print ("Measured Distance = %.1f cm" % dist2)
                    s.send(MESSAGE8)
                    subprocess.run(["python","Seq2.py"])
                    time.sleep(1)
                    subprocess.run(["python","Seq2.py"])
                    s.send(MESSAGE2)
                    time.sleep(3.5)
                    subprocess.run(["python","Seq1.py"])
                    time.sleep(1)
                    subprocess.run(["python","Seq1.py"])
                    
                elif dist2 >= 18 and dist2 <= 25:
                    count = count + 1
                    print (count)
                    if count == 1:
                        print ("Measured Distance = %.1f cm" % dist2)
                        s.send(MESSAGE3)
                        subprocess.run(["python","Seq2.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq2.py"])
                        s.send(MESSAGE2)
                        time.sleep(3.5)
                        subprocess.run(["python","Seq3.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq3.py"])
                    
                    elif count == 2:
                        print ("Measured Distance = %.1f cm" % dist2)
                        s.send(MESSAGE3)
                        subprocess.run(["python","Seq2.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq2.py"])
                        s.send(MESSAGE2)
                        time.sleep(3.5)
                        subprocess.run(["python","Seq3.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq3.py"])
                    
                    elif count == 3:
                        print ("Measured Distance = %.1f cm" % dist2)
                        s.send(MESSAGE3)
                        subprocess.run(["python","Seq2.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq2.py"])
                        s.send(MESSAGE2)
                        time.sleep(3.5)
                        subprocess.run(["python","Seq3.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq3.py"])
                    
                     
                    elif count == 4:
                        print("gg")
                        s.send(MESSAGE16)
                        subprocess.run(["python","Seq2.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq2.py"])
                        s.send(MESSAGE2)
                        time.sleep(6.5)
                        subprocess.run(["python","Seq3.py"])
                        time.sleep(1)
                        subprocess.run(["python","Seq3.py"])
                    
                        
                        
                    
                    
                    
                    
                 
                    
                
                    
  
                
               
                    
                    
        except KeyboardInterrupt:
            print("Measurement stopped by User")
                
             
       

    
        
        
