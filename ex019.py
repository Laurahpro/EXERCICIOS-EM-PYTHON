# ==== Exercício 19 ====
from random import choice
alu1 = input('Primeiro aluno: ')
alu2 = input('Segundo aluno: ')
alu3 = input('Terceiro aluno: ')
alu4 = input('Quarto aluno: ')
print('O aluno selecionado é para apagar o quadro é {}'.format(choice([alu1, alu2, alu3, alu4])))