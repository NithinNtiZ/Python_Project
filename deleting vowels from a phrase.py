#deleting vowels from a phrase


n= input("Enter a Phrase : ")
x= ""
for letter in n:
    if letter in "aieou" :
        x=x+ ""
    else:
        x=x+ letter

print (x)
