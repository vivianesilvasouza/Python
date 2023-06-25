""" introduçao ao try/exceptt """

numero_str = input ('vou dobrar o número que vc digitar: ') 

try:
    numero_float = float(numero_str)
    print('FLOAT:',numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
except :
    print('isso não é um número')

