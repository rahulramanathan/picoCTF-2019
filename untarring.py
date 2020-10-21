import os
import tarfile
num = 1000
while num>1:
    filename =  str(num)+".tar"
    tar = tarfile.open(filename)
    tar.extractall()
    tar.close()
    os.remove(filename)
    num = num - 1
