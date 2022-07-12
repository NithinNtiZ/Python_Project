list= [0,1,3,4,5,6,8,9,]

n=len(list)
 
#print(n)

for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                sum=(list[i]+list[j]+list[k]+list[l])
                if sum%2>0:
                    num=list[i],list[j],list[k],list[l]
                    print(num)