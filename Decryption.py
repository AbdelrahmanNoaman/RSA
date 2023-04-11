from GenerateNumbers import *

def decrypt(cipherText,DecKey,N):
    M=pow(cipherText,DecKey)%N
    textMsg=decode(M)
    return textMsg