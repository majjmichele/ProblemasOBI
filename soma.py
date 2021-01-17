a, b = [int(i) for i in input().split()] #quantidade de valores, valor da soma
frase = input() #valores

lista_numeros = [int(i) for i in frase.split()]  #conversão de valores

conta = 0
soma = 0
c = 0

while c < a:
    d = c+1
    soma = lista_numeros[c]
    if soma == b:
            conta += 1

    while d < a:
        soma += lista_numeros[d]
        if soma == b:
            conta += 1
        d+=1
    c+=1

print(conta)