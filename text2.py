a = 2
b = 2
c = 2

while (a <= b and a < c) or (b > c):
    a = a + 1
    if a <= c:
        b = b - 1
    else:
        c = c + a

# À la fin de la séquence, afficher les valeurs de a, b et c
print("À la fin de la séquence :")
print("a =", a)
print("b =", b)
print("c =", c)
