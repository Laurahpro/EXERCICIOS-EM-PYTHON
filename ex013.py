print('-' * 20)

Funcionário = (input('Nome do Funcionário: '))
Cargo = (input('Seu cargo: '))
salario = float (input('Escreva o valor do salário: R$ '))
percent = int (input('Qual o percentual? '))
novo = salario + (salario * percent / 100)
print ('O valor antigo do salário era R$ {:.2f}, com aumento de {} % passa a ser de R$ {:.2f}'.format(salario, percent, novo)) 
print('-' * 20)
