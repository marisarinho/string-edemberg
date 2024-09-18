string=input('')
for i in range(len(string)):
    a=string[i]*(i+1)
    print(a)
for j in range(len(string)-2,-1,-1):
    b=(j+1)*string[j]
    print(b)
