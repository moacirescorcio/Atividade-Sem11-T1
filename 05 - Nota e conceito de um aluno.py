nota = 0
while True:
    nota = float(input('Insira a nota: '))
    if nota < 0 or nota > 10:
        print('Nota inválida.')
    elif nota >= 8.5:
        print('Conceito do aluno: A')
        break
    elif nota >= 7:
        print('Conceito do aluno: B')
        break
    elif nota >= 5:
        print('Conceito do aluno: C')
        break
    elif nota >= 4:
        print('Conceito do aluno: D')
        break
    elif nota >= 0:
        print('Conceito do aluno: E')
        break
    