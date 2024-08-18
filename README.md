# Basic X-Plane Data Ref
Basic X-Plane 12 UDP Socket programming using Python

# Additional readings

    Socket - https://docs.python.org/3/library/socket.html#example
    Struct - https://docs.python.org/3/library/struct.html#examples
    
    XPlane datarefs:
    https://developer.x-plane.com/datarefs/
    https://github.com/der-On/X-Plane-Dataref-Search/blob/master/dist/DataRefs.txt


# Struct message/data

X-Plane's interface is described using C language structures and expects a particular size and properly encoded data. We have to format ('pack') python data into a proper structure before sending it, and unpack any received data.

The easiest way to pack and unpack is to use the python `struct` module. 

**For example:**

    cmd = b'RREF'
    freq = 1
    index = 1
    msg = struct.pack("<4sxii400s", cmd, freq, index, b'sim/flightmodel/forces/g_axil')

The string `<4sxii400s` describes how to pack the data:

    `<`				little endian (i.e., least significant byte in the lowest memory position)
    `4s`				a 4-byte object, commonly string, 'RREF', expressed as a bytes: b'RREF'.
    `x`				a null byte, or 0x00. X-Plane is looking for a null-terminated 4-character string & this encodes the null value.
    `i`				a 4-byte integer
    `i`				another 4-byte integer (you could also combine these as `2i`, which consumes two integer arguments)
    `400s`				a 400-byte object. Note that Python pads and zero-fills to fit 400 bytes.

# Data Refs

    RREF <freq><index><dataref/channel>


# Requirements

* Python 3
* Running X-Plane 12

