from GenerateNumbers import *

def decrypt(cipherText,DecKey,N):
    blocks=cipherText.split('-')
    finalText=""
    for block in blocks:
        M=pow(int(block),DecKey,N)
        textMsg=decode(M)
        finalText+=textMsg
    return finalText