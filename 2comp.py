n=input('frase').upper()
cripto=''
for i in n:
    if i=='A':
        cripto+=' '
    elif i=='E':
        cripto+='U'
    elif i=='I':
        cripto+='O'
    elif i=='O':
        cripto+='I'
    elif i=='U':
        cripto+='E'
    elif i==' ':
        cripto+='A'
    else:
        cripto += i
print(cripto)
