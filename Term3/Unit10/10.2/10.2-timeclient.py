"""
File: timeclient.py
Project 10.2
Client for obtaining the day and time. Recovers from connection
errors.
"""

from socket import socket, AF_INET, SOCK_STREAM
from codecs import decode

HOST = "localhost" 
PORT = 5000
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

def connectServer(s):
    s.connect(ADDRESS)
    dayAndTime = decode(s.recv(BUFSIZE), 'ascii')
    print(dayAndTime)
    s.close()

server = socket(AF_INET, SOCK_STREAM)           # Create a socket

try:
    connectServer(server)

except ConnectionRefusedError as e:
    print(f">>> Error connecting to server: \n    {e}")

    
