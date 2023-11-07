"""
Repetições
enquanto (enquanto)
Executa uma ação enquanto uma condição para verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador  =  0

while  contador  <=  100 :
    contador  +=  1

    if  contador  ==  6 :
        print ( 'Não vou mostrar o 6.' )
        continuar

    if  contador  >=  10  and  contador  <=  27 :
        print ( 'Não vou mostrar o' , contador )
        continuar

    print( contador )

    if  contador  ==  40 :
        quebrar


print ( 'Acabou' )