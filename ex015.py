Nome = input('Seu nome: ')
dias = int (input('Quantidade de dias alugados: '))
km = float (input('Quantidade de Km rodados: '))
diária = float (input('Valor da diária: '))
CustoKm = float (input('Custo Km: '))
pagar = (dias * diária) + (km * CustoKm)
print ('{}, Você usou o carro por {:.0f} dias, tendo percorrido {:.0f} Kms. O valor da diária é de R$ {:.2f} e o Custo por Km é de R$ {:.2f}, sendo assim, o valor total a pagar é de R$ {:.2f}.'.format(Nome, dias, km, diária, CustoKm, pagar))

