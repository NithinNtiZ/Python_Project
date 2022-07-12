3#


sum=0
b=100
num= []

n=int(input("enter number of item "))
if n>100:
    print("enter value under 100")
else:
    for i in range(n):
        num.append(input("enter price of item "+ str(i+1) + ': '))
        
        sum=sum+int(num[i])

        a=b-int(num[i])
        b=a
        if b>=0:
            print("remaining money :",a)
        else:
            
            print("can't buy price is too high ")
    



#print(num)

