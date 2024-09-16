s=input('frase ')
n=int(input('numero '))
vogais='aeiou'
py=''
for letra in s:
    if letra in vogais:
        for j in range(n):
            py+=letra
            # print(letra,end='')
    else:
        py+=letra
        
print(py)
