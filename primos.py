def esPrimo(numero):
    if numero == 0 or numero == 1:
        return False
    
    if numero == 4:
        return False

    for indice in range(2, numero // 2 + 1):
        if numero % indice == 0:
            return False

    return True

primos = []

for indice in range(1, 250):
    if esPrimo(indice):
        primos.append(indice)
