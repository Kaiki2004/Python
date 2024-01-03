from random import randint

def advinhar(palavras):
  palavra = palavras[randint(0, 9)]
  ocult = []
  chance = randint(6, 11)
  for c in range(len(palavra)):
    ocult.append('')

  print('Você terá %d chances para adivinhar a palavra!' %chance)
  print('Essa palavra possui %d letras!' %(len(ocult)))
  print(ocult)

  while chance != 0:
    letra = str(input('Informe uma letra: ').upper())
    indice = 0
    achou = False
    venceu = False
    for z in range(len(palavra)):
      if letra == palavra[z]:
        indice = z
        ocult[z] = letra
        achou = True

    if achou == True:
      print('Você acertou a letra!')
      print('Você tem %d chances para adivinhar a palavra!' %chance)
      print(ocult)
    elif achou == False:
      print('Essa palavra não possui essa letra, tente novamente')
      print(ocult)
      chance = chance - 1
      print('Você tem %d chances para adivinhar a palavra!' %chance)


    for b in range(len(ocult)):
      if '' not in ocult:
        chance = 0
        venceu = True

    if venceu == True and chance == 0:
      print('Você acertou! a palavra oculta era: %s' %palavra)
    elif venceu == False and chance == 0:
      print('Suas chances acabaram, você perdeu!')






palavras = []
with open("text.txt", "r", encoding="utf-8") as arquivo:
  for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha.upper())



print("Jogo de adivinhar a palavra!")
advinhar(palavras)