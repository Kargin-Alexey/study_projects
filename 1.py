from math import sqrt
from numpy import array,append

nu = int(input())
def sum_of_squares(n):
    a= int(sqrt(n))
    mass = array([a])
    for i in range(1,5):
        if (a == 0) or (n- a**2) <= 0:
            return [len(mass),mass]
            break
        Ai = int(sqrt(n - a**2))
        mass = append(mass,Ai)
        n -= a ** 2
        a = Ai
k = sum_of_squares(nu)
print(k[0])
for j in range(len(k[1])):
    print(k[1][j], end = " ")