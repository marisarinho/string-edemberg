n=input(' ')
a=n.split(' ')
print(f'{a.pop(-1)},',end='')
for i in a:
    print(f'{i[0]}.',end=' ')
