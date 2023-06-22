""" interpolação básica de strings 

s - String 
d e i - int 
f - float 
x e x - hexadecimal (ABCDEF123456789) """


nome = 'Viviane'
preco = 100.958976
varial = '%s, o preço é R$%.2f' % (nome, preco)
print(varial)
print('o hexadecimal de %d é %04x' % (15, 15))