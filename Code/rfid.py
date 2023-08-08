import socket
import subprocess
import time

TCP_IP = '192.168.254.11'
TCP_PORT = 5612
BUFFER_SIZE = 1024

MESSAGE = b'Bonnie'
MESSAGE1 = b'Freddy'
MESSAGE2 = b'Chica'
MESSAGE3 = b'Marionette'
MESSAGE4 = b'Balloon Boy'
MESSAGE5 = b'Foxy'
MESSAGE6 = b'0'





s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))




while True:
    data=s.recv(BUFFER_SIZE)
    print(data)
    if data == b'Bonnie':
        s.send(MESSAGE)
        time.sleep(1)
        s.send(MESSAGE6)
        bonnie = subprocess.Popen(["python","bonnie.py"])
        time.sleep(2)
        
    elif data == b"TerminateBonnie":
        bonnie.terminate()
        print("process terminated")
        time.sleep(2)
        
    elif data == b'Freddy':
        s.send(MESSAGE1)
        time.sleep(1)
        s.send(MESSAGE6)
        freddy = subprocess.Popen(["python","freddy.py"])
        time.sleep(2)
    
    elif data == b"TerminateFreddy":
        freddy.terminate()
        print("process terminated")
        time.sleep(2)
        
    elif data == b'Chica':
        s.send(MESSAGE2)
        time.sleep(1)
        s.send(MESSAGE6)
        chica = subprocess.Popen(["python","chica.py"])
        time.sleep(2)
    
    elif data == b"TerminateChica":
        chica.terminate()
        print("process terminated")
        time.sleep(2)
        
    elif data == b'Marionette':
        s.send(MESSAGE3)
        time.sleep(1)
        s.send(MESSAGE6)
        marionette = subprocess.Popen(["python","marionette.py"])
        time.sleep(2)
    
    elif data == b"TerminateMarionette":
        marionette.terminate()
        print("process terminated")
        time.sleep(2)
        
    elif data == b'Balloon Boy':
        s.send(MESSAGE4)
        time.sleep(1)
        s.send(MESSAGE6)
        balloonboy = subprocess.Popen(["python","balloonboy.py"])
        time.sleep(2)
    
    elif data == b"TerminateBalloon Boy":
        balloonboy.terminate()
        print("process terminated")
        time.sleep(2)
        
    elif data == b'Foxy':
        s.send(MESSAGE5)
        time.sleep(1)
        s.send(MESSAGE6)
        foxy = subprocess.Popen(["python","foxy.py"])
        time.sleep(2)
    
    elif data == b"TerminateFoxy":
        foxy.terminate()
        print("process terminated")
        time.sleep(2)
        
        
        
        
        
        
        
        
        
    
        
        
        

    

    

