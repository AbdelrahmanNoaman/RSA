from GenerateNumbers import *

def encrypt(message,EncKey,N):
    M=encode(message)
    C=pow(message,EncKey)%N
    return C
    


