import socket
import struct
import binascii

rawsocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))      #0x0800 is ethernet type for IP

pkt = rawsocket.recvfrom(2048)

ethernetHeader = pkt[0][:14]                          #first 14 bytes are of ethernet header
eth_hdr = struct.unpack("!6s6s2s",ethernetHeader)     # network byte order (! or >) Big-endian
des_mac = binascii.hexlify(eth_hdr[0])
src_mac = binascii.hexlify(eth_hdr[1])
eth_type = binascii.hexlify(eth_hdr[2])

ipheader = pkt[0][14:34]
ip_hdr = struct.unpack("!12s4s4s",ipheader)
print "Source ip is: " + socket.inet_ntoa(ip_hdr[1])
print "Destination ip is: " + socket.inet_ntoa(ip_hdr[2])

tcpheader = pkt[0][34:54]
tcp_hdr = struct.unpack("!HH16s", tcpheader)
print tcp_hdr