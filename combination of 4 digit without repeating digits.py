def comb(a):
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if(i!=j and i!=k and j!=k and l!=i and j!=l and k!=l):
                        print (a[i] ,a[j], a[k],a[l])



comb([1,3,5,8])