num = 10
salida = ''
a = (num + 1) / 2
a = int(a)
# print(type(a))
#print (a)
renglones = a
i = 1
n = 1

for r in range(renglones):
    salida = '  ' * a + ' '.join(str(i) for i in range(1, n+1))
    print(salida)
    a = a-1
    n = n+2
