# exercicio 1 (ac1)

# elabore um codigo para resolver a função de segundo grau
# ax**2 + bx + c = 0
a  = int(input("digite o valor do coeficiente a: "))
b  = int(input("digite o valor do coeficiente b: "))
c  = int(input("digite o valor do coeficiente c: "))
# delta = b**2 . 4ac
delta = b**2 - 4*a*c
if delta >+0>:
else:
    print("não existe valor real")
print("o valor de delta é:  ", delta)
# x =(-b + - raiza(delta))/2a
x1 = (-b - delta**0.5) / (2*a)
x2 = (-b + delta**0.5) / (2*a)
print(" o valor de x1 é: ", x1)
print(" o valor de x2 é: ", x2)


# exercicio 2 (ac1)

# elabore um programa python que leia uma variavel inteira (ano)
# mostre se o ano é bissexto ou nao 
ano = int(input("digite o ano que voce quer analisar"))

bissexto = (ano % 4 == 00 and (ano %  100 != 00 or ano % 400 == 00))
print("seu ano bissexto é", bissexto) and print("seu ano bissexto é", bissexto)





