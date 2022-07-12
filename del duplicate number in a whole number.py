n=input("Enter any number  : ")

l=list(str(n))

m= []

for i in l:
    if i not in m:
        m.append(i)
        m.sort()
#print("The list is :", list(m))


b=""
x=b.join(m)

print("After deleting dupliacte and sorting  : ", x)