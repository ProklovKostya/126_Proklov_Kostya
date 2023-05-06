def eqv(A, B, C):
    eps = 0.0001 * max(A, B)
    return abs(A + B - C) <= eps

# пример значений
A = 12345.67
B = 6789.01
C = 19134.68

if eqv(A, B, C):
    print("Сумма A и B равна C с учетом точности eps.")
else:
    print("Сумма A и B не равна C с учетом точности eps.")