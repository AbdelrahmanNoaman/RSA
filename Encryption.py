from GenerateNumbers import *

def encrypt(PlainText,EncKey,N):
    M=encode(PlainText)
    C=pow(M,EncKey,N)
    return C
    


