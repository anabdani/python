"""
Formatação básica de strings
s - corda
d-int
f - flutuar
.<número de dígitos>f
x ou X - Hexadecimal
(Caracteres)(><^)(quantidade)
> - Esquerda
< - Direita
^ -Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Sinalizadores de conversão - !r !s !a
"""
variável  =  'ABC'
print ( f' { variável } ' )
print ( f' { variável : >10 } ' )
print ( f' { variável : <10 } .' )
print( f' { variável : ^10 } .' )
print ( f' { 1000.4873648123746 :0=+10,.1f } ' )
print ( f'O hexadecimal de 1500 é { 1500 :08X } ' )
print ( f' { variável !r } ' )