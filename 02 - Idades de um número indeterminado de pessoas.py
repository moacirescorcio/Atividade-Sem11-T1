quantidade = 0
pessoas = -1
idade = 0
lista = []
soma = 0
while True:
    idade = int(input())
    soma += idade
    pessoas += 1
    if idade > 0:
        lista.append(idade)
    if idade == 0: break

media = soma / pessoas
maior = max(lista)
menor = min(lista)
print(pessoas)
print(f'{media:.2f}')
print(menor)
print(maior)
