"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1


print('Acabou')



"""
Iterando strings com while
"""
#       012345678910
#nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
#tamanho_nome = len(nome)
#print(nome)
#print(tamanho_nome)
#print(nome[3])

#nova_string = ''
#nova_string += '*L*u*i*z* *O*t*á*v*i*o'




"""
Iterando strings com while
"""
#       012345678910
# nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321


nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)