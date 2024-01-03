def somatorio(N):
  fat = 1
  for c in range(2, (N+1), 1):
    fat = fat + (c / (c * c))
  return fat




N = int(input('Informe o valor de N: '))
result = somatorio(N)
print('Somatório: %0.2f' %result)