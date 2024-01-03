def menorValor(a, b):
  if (a < b):
    print(f'{a} é o menor vlor')
  elif (a > b):
    print(f'{b} é o menor valor')
  else:
    print('Os valores são iguais.')

x = int(input('Valor 1: '))
y = int(input('Valor 2: '))
menorValor(x,y)
