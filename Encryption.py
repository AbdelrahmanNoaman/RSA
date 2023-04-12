from GenerateNumbers import *

def prepareForEncryption(Msg):
    Msg=Msg.lower()
    while(len(Msg)%5!=0):
        Msg+=" "
    return Msg

def encrypt(PlainText,EncKey,N):
    cipherText=""
    PlainText=prepareForEncryption(PlainText)
    for i in range(len(PlainText)//5):
        M=encode(PlainText[5*i:5*i+5])
        C=pow(M,EncKey,N)
        cipherText+=str(C)
        if(i!=(len(PlainText)//5 -1)):
            cipherText+="-"
    return cipherText
    


