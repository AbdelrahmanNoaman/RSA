from GenerateNumbers import *
from Encryption import *
from Decryption import *

Msg="ya no3 enta bt3ml eh ybnl mgnn "
while(len(Msg)%5!=0):
    Msg+=" "
publicKey,N,privateKey=GenerateRequiredNumbers()
finalText=""
print(len(Msg))
for i in range(len(Msg)//5):
    cipherText=encrypt(Msg[5*i:5*i+5],publicKey,N)
    finalText+=decrypt(cipherText,privateKey,N)
    print(finalText)