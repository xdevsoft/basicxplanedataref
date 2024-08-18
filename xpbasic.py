# -*- coding: utf-8 -*-
#!/usr/bin/env python3
 
import socket
import struct

# Demo UDP socket programming for XPlane 12 Data Refs
# Additional readings:
# Socket - https://docs.python.org/3/library/socket.html#example
# Struct - https://docs.python.org/3/library/struct.html#examples

# Command
command = b'RREF'
# Number of data per seconds
frequency = 1
# Unique identifier per command or request
index = 1
# Message channel
channel = b'sim/flightmodel/forces/g_axil'
# change this based on your XPlane computer ip address
IP = '192.168.1.36'
# Standard or default port number for XPLane 12
PORT = 49000

# Create a socket or instantiate it
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# This line will create or assemble the message package
msg = struct.pack(
    '<4sxii400s', command, 
    frequency, index, channel
)
# This line will send the message based on the given ip address and port
s.sendto(msg, (IP, PORT))

# This line will block or wait for the message from XPlane 12
# It will return a tuple 
data, addr = s.recvfrom(1024)
# We are only ineterested with the data starting from index 5 to 13 from the bytes 'data'
idx, value = struct.unpack('<if', data[5:13])

print(idx, value)