def valorPagamento(v,d):
  if d == 0:
    p = v
  else:
    tx = (v*0.03) + ((v*0.001)*d)
    p = v + tx
  return p
valor = ''
cont = 0
valorTotal = 0
while valor != 0:
  valor = float(input('Digite o valor das prestações '))
  dias = int(input('Digite os dias de atraso da prestação '))
  resu = (valorPagamento(valor,dias))
  valorTotal = valorTotal + resu
  cont = cont + 1
  print(f'valor a pagar ', resu)

print('finalizado')
print(f'quantidade de prestações pagas ',(cont-1))
print(f'valor total das prestações ',valorTotal)
