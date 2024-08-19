# Basic X-Plane Data Ref
Basic X-Plane 12 UDP Socket programming using Python

I wrote it while I'm exploring X-Plane 12 and I'm planning to create my own 3DOF motion simulation rig.
I will also improved and extend this simple example and you will also see how it will be used.

That's why I want to share my experience and adventure while I'm building it.

# Additional readings

    Socket - https://docs.python.org/3/library/socket.html#example
    Struct - https://docs.python.org/3/library/struct.html#examples
    
    XPlane datarefs:
    https://developer.x-plane.com/datarefs/
    https://github.com/der-On/X-Plane-Dataref-Search/blob/master/dist/DataRefs.txt


# Struct message/data

X-Plane's interface is described using C language structures and expects a particular size and properly encoded data. We have to format ('pack') python data into a proper structure before sending it, and unpack any received data.

The easiest way to pack and unpack is to use the python `struct` module. 

**Structure**

    RREF <freq><index><dataref/channel>

**Example:**

    command = b'RREF'
    frequency = 1
    index = 1
    channel = b'sim/flightmodel/forces/g_axil'
    msg = struct.pack('<4sxii400s', command, frequenct, index, channel)

The string `<4sxii400s` describes how to pack the data:

    `<`				little endian (i.e., least significant byte in the lowest memory position)
    `4s`				a 4-byte object, commonly string, 'RREF', expressed as a bytes: b'RREF'.
    `x`				a null byte, or 0x00. X-Plane is looking for a null-terminated 4-character string & this encodes the null value.
    `i`				a 4-byte integer
    `i`				another 4-byte integer (you could also combine these as `2i`, which consumes two integer arguments)
    `400s`				a 400-byte object. Note that Python pads and zero-fills to fit 400 bytes.

**Sample packed message:**

    b'RREF\x00\x01\x00\x00\x00\x01\x00\x00\x00sim/flightmodel/forces/g_axil\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

# IP address and port

    # change this based on your XPlane computer ip address
    IP = '192.168.1.36'
    # Standard or default port number for XPLane 12
    PORT = 49000

# Create a socket / instantiate an object

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
socket.AF_INET is a constant that represent the address (and protocol) families
socket.SOCK_DGRAM is constant that represent the socket types

# Sending socket message

This function sends data to a socket we created or instantiated, and it requires a tuple of IP and PORT of the X-Plane

    s.sendto(msg, (IP, PORT))

**Sample message to be sent:**

    b'RREF,\x01\x00\x00\x00~\xef\x04\xbd'

# Receiving socket message

    # This line will block or wait for the message from XPlane 12
    # It will return a tuple
    data, addr = s.recvfrom(1024)
  
**Method Signature/Syntax:**

socket.recvfrom(bufsize[, flags])

**Parameters:**

bufsize - The number of bytes to be read from the **UDP socket.**

flags - This is an optional parameter. As supported by the operating system. Multiple values combined together using bitwise OR. The default value is zero.

# Unpacking the message / data

UDP packets will have header RREF and include the index you passed during the request (that’s how you’ll know which dataref this is) and a single floating point value.

    # We are only interested with the data starting from index 5 to 13 from the bytes 'data'
    idx, value = struct.unpack('<if', data[5:13])

The string `<if` describes how to pack the data:

    `<`				little endian (i.e., least significant byte in the lowest memory position)
    `i`				a 4-byte integer
    `f`				a 4-byte float

# Printing the data we received

    print(idx, value)

**Sample received and printed data:**

    1 -0.0324549600481987

# Requirements

* Python 3
* Running X-Plane 12

# My Current Setup

 - Steam version 1721173382
 - X-Plane version 12.1.1  
 - Ubuntu Linux 20.04 (Steam & X-Plane)
 - Development/Client Laptop
	 - Linux / Python 3.10.12
	 - Mac / Python 3.12.2

# What's next?

 - Received data continuously 
 - Subscribe to multiple channels
 - Use callback and event
 - Get X-Plane IP and port dynamically
 - Use threading

 

