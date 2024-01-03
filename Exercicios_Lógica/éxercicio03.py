vet = []
notas = []
media = 0
soma = 0

n = int(input('inrforme a quatidade de alunos '))
for i in range(n):
  notas.append(int(input(f'informe a nota do aluno {i+1} ')))
  soma = soma + notas[i]

media = soma / n
print(f'A média é {media}')
for i in range(n):
  if(notas[i] >= media):
    print(f'Nota acima da média {notas[i]}')
