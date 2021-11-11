op = 0
while True:
    print('''OPÇÕES:
1 - SAUDAÇÃO
2 - BRONCA
3 - FELICITAÇÃO
0 - FIM''')
    op = int(input())
    if op == 1:
        print('1 - Olá. Como vai?')
    elif op == 2:
        print('2 - Vamos estudar mais.')
    elif op == 3:
        print('3 - Meus Parabéns!')
    elif op == 0:
        print('0 - Fim de serviço.')
        break
    else:
        print('Opção inválida.')