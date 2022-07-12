n=int(input("enter "))
sum=0
a = list(range(0,n))

for i in range(0,n):
    a[i]=input("enter a num ")

for i in range(0,n):
    sum=sum+int(a[i])

print("SUM OF ALL THE NUMBERS ",sum)
