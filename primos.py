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

for indice in range(1, 251):
    if esPrimo(indice):
        primos.append(indice)

with open('results.txt', 'w') as archivo:
    for primo in primos:
        archivo.write(str(primo) + '\n')
