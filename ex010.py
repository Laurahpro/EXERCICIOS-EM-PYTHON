print('        Casa de Cambio')
print('-' * 35)
nome = (input('Digite seu nome: '))
end = (input('Digite seu endereço: '))
idade = (input('Digite sua idade: '))
real = float(input('Quanto dinheiro você quer trocar: R$ '))
dolar = real / 5.50 
euro = real / 5.96
libra = real / 6.85 
print('Com R$ {:.2f} você pode comprar US$ {:.2f} dólares, ou {:.2f} euros, ou {:.2f} libras'.format(real, dolar, euro, libra))