larg = float (input('Largura da parede: '))
alt = float (input('Altura da parede: '))
área = larg * alt 
print ('Sua parede tem a dimensão de {}x{} e sua área é de {}mts²'.format(larg, alt, área))
tinta = área / 2 
print('Você vai precisar de {} litros de tinta!'.format(tinta))