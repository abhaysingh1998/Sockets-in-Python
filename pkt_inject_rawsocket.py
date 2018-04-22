import struct
import socket

rawsocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))
rawsocket.bind(("wlp6s0", socket.htons(0x0800)))

packet = struct.pack("!6s6s2s",'\xaa\xaa\xaa\xaa\xaa\xaa','\xbb\xbb\xbb\xbb\xbb\xbb','\x08\x00')

rawsocket.send(packet + "Hello There !!")