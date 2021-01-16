'''
    A idade da mãe é a soma da idade dos filho, solução do problema
    tem como objetivo encotrar a maior idade dos três filho de Mônica
'''
M = int(input())  #idade da mãe
A = int(input())  #idade do 1 filho
B = int(input())  #idade do 2 filho
C = M - (A+B)  #idade do 3 filho

#Casos de teste 14 18 20 - 9 17 21
maior_idade = (max(A, max(B, C)))
print(maior_idade)