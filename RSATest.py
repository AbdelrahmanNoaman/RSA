from GenerateNumbers import *
from Encryption import *
from Decryption import *
finalText=""
Msg="ya nu3man"
publicKey,N,privateKey=GenerateRequiredNumbers()
cipherText=encrypt(Msg,publicKey,N)
finalText+=decrypt(cipherText,privateKey,N)
print(finalText)