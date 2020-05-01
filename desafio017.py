import math 
ca = int(input('Digite o valor do cateto adjacente: '))
co = int(input('Digite o valor do cateto oposto: '))
hi = math.sqrt((math.pow(ca,2)+math.pow(co,2)))
print('O valor da hipotenusa é {:.2f}'.format(hi))