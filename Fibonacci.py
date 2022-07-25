# n = 13
n = 10


a = 0

b = 1

print(f"{a} -> {b}", end = "")

c = 3

existe = False

while c <= n:

    d = a + b

    if d == n:
        existe = True


    print(f" -> {d}", end = "")

    a = b

    b = d

    c += 1

if existe == True:
    print("\nO número existe na sequência de Fibonacci!")

else: 
    print("\nO número NÃO existe na sequência de Fibonacci!")

print('-> FIM')