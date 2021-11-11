soma = 0
n = 0
while True:
    n = int(input('Insira um número: '))
    soma += n
    if n == 0: break
    
print(f'A soma desses números é igual a {soma}')