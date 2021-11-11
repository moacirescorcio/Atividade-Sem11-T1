h = 0
c = 0
m = 0
a = 0
q = 0
x = 0
codigo = 0
total = 0
while True:
    print('''CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')
    codigo = input().lower()
    if 'h' in codigo:
        h += 1
        total += 5.5
    elif 'c' in codigo:
        c += 1
        total += 6.8
    elif 'm' in codigo:
        m += 1
        total += 4.5
    elif 'a' in codigo:
        a += 1
        total += 7
    elif 'q' in codigo:
        q += 1
        total += 4
    elif 'x' in codigo:
        print(f'{total:.2f}')
        break
    
    