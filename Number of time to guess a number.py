import random
score=0

n=int(input("Enter a Number :"))
z=int(input("Enter the number to be guess :"))



while True:
    x= int(random.randint(0,n))
    if x == z:
        print("congrates you got it !")
        break
                
    else:
        score+=1
        continue    
print("It took",score,"times to correctly guess ",z)