def tribonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

def triangulo_invertido(n):
    if n == 0:
        return
    print('*' * n)
    triangulo_invertido(n - 1)

def triangulo_invertido_pt2(n, aux = 1):
    if n == 0:
        return
    print('*' * aux)
    triangulo_invertido_pt2(n - 1, aux + 1)
    #pura gambiarra mas funciona