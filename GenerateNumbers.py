import random

def isPrime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def generateRandomPrimeNumber():
    while(True):
        num=random.randint(0,(2**2048)-1)
        if(isPrime(num)):
            break

def GCD(number1,number2):
    if(number2==0):
         return number1
    return GCD(number2,number1%number2)      

def GenerateE(PhiN):
    while(True):
        num=random.randint(0,PhiN-1)
        if(GCD(num,PhiN)==1):
            break

def GenerateD(E,PhiN):
    return pow(E,-1,PhiN)        

