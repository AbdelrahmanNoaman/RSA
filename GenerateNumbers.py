import random

def isPrime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def generateRandomPrimeNumber():
    while(True):
        num=random.randint(2,(2**32)-1)
        if(isPrime(num)):
            break
    return num    

def GCD(number1,number2):
    if(number2==0):
         return number1
    return GCD(number2,number1%number2)      

def GenerateE(PhiN):
    while(True):
        num=random.randint(0,PhiN-1)
        if(GCD(num,PhiN)==1):
            break
    return num    

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    

def GenerateD(E,PhiN):
    return modinv(E,PhiN) 

def convCharToNum(c):
    if(ord(c)>=97 and ord(c)<=122):
        return ord(c)-87
    if(ord(c)>=48 and ord(c)<=57):
        return ord(c)-48
    return 36

def convNumToChar(num):
    if(num>=10 and num <=35):
        return ord('a')+num-10
    if(num>=0 and num <=9):
        return ord('0')+num
    return 32

def encode(s):
    counter=0
    for i in range(5):
        charValue=convCharToNum(s[i])
        counter+= charValue*pow(37,4-i)
    return counter  

def decode(s):
    group="" 
    for i in range(5):
        value=int(s/(pow(37,4-i)))
        group+=chr(convNumToChar(value))
        s=s%(pow(37,4-i))
    return group 


def GenerateRequiredNumbers():
    p=generateRandomPrimeNumber()
    q=generateRandomPrimeNumber()
    N=p*q
    phiN=(p-1)*(q-1)
    e=GenerateE(phiN)
    d=GenerateD(e,phiN)
    return e,N,d



