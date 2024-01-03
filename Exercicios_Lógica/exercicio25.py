import random

# Lista de palavras
palavras = ['python', 'forca', 'jogo', 'palavra', 'oculta', 'programacao', 'diversao', 'computador', 'desenvolver', 'aprender']

palavra_secreta = random.choice(palavras).lower()


letras_corretas = []
letras_incorretas = []
tentativas_restantes = 8  # Número fixo de tentativas


letras_tentadas = []

palavra_oculta = '_' * len(palavra_secreta)

while tentativas_restantes > 0 and palavra_oculta != palavra_secreta:
    print("\nPalavra: ", ' '.join(palavra_oculta))

    print("Tentativas restantes:", tentativas_restantes)

    if letras_tentadas:
        print("Letras já tentadas:", ' '.join(letras_tentadas))


    letra = input("Digite uma letra: ").lower()


    if letra in letras_tentadas:
        print("Você já tentou esta letra. Tente outra.")
        continue

    letras_tentadas.append(letra)


    if letra in palavra_secreta:
        letras_corretas.append(letra)
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                palavra_oculta = palavra_oculta[:i] + letra + palavra_oculta[i+1:]
        if palavra_oculta == palavra_secreta:
            print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
            break
    else:
        letras_incorretas.append(letra)
        tentativas_restantes -= 1
        print("Letra incorreta! Tente outra.")

if tentativas_restantes == 0:
    print("Acabaram as tentativas! A palavra era:", palavra_secreta)