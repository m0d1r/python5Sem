import math
#N^2-N-10=4N+40
#n^2-5n-50 = 0

a = 1
b = -5
c = -50

D = b**2 - 4*a*c

if D >= 0:
    N1 = (-b + math.sqrt(D)) / (2*a)
    N2 = (-b - math.sqrt(D)) / (2*a)
    
    print(f"Корни уравнения: N1 = {N1}, N2 = {N2}")
    
    valid_roots = [n for n in (N1, N2) if n > 0 and n % 1 == 0]
    
    for n in valid_roots:
        n = int(n)
        T1 = n**2 - n - 10
        T2 = 4*n + 40
        print(f"\nПодходящий размер массива: N = {n}")
        print(f"T1 = {n}^2 - {n} - 10 = {T1}")
        print(f"T2 = 4*{n} + 40 = {T2}")
else:
    print("Нет действительных корней")