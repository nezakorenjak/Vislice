

def prastevila_do(n):
    seznam = [2]
    for n in range(2, n+1):
        for i in seznam:
            if n % i == 0:
                break
        seznam.append(n)
    return seznam

print(prastevila_do(200))