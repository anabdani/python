"""
import random

def escolher_palavra():
    palavras = ["python", "programacao", "jogo", "computador", "desenvolvimento"]
    return random.choice(palavras)

def exibir_palavra_oculta(palavra, letras_corretas):
    palavra_oculta = ""
    for letra in palavra:
        if letra in letras_corretas:
            palavra_oculta += letra
        else:
            palavra_oculta += "*"
    return palavra_oculta

def jogo_da_forca():
    palavra_secreta = escolher_palavra()
    tentativas_maximas = 6
    letras_corretas = []
    tentativas = 0

    print("Bem-vindo ao Jogo da Forca!")
    print(exibir_palavra_oculta(palavra_secreta, letras_corretas))

    while tentativas < tentativas_maximas:
        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite uma única letra.")
            continue

        if letra in letras_corretas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra_secreta:
            letras_corretas.append(letra)
            print("Letra correta!")
        else:
            tentativas += 1
            print(f"Letra incorreta! Tentativas restantes: {tentativas_maximas - tentativas}")

        palavra_oculta = exibir_palavra_oculta(palavra_secreta, letras_corretas)
        print(palavra_oculta)

        if palavra_oculta == palavra_secreta:
            print("Parabéns! Você acertou a palavra!")
            break

    if tentativas == tentativas_maximas:
        print(f"Fim de jogo. A palavra correta era: {palavra_secreta}")

if __name__ == "__main__":
    jogo_da_forca()
    """

"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            print(letra_secreta)
        else:
            palavra_formada += '*'

print('Palavra formada:', palavra_formada)

if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0