preço = float (input('Preço do produto: R$ '))
novo = preço - (preço * 8 / 100)
print('O produto que custava {:.2f} com o desconto da promoção, vai custar {:.2f}.'.format(preço, novo)) 
