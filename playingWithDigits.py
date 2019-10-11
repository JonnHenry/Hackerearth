import math

def suma_de_digitos(numero):
    sumDigit = 0
    while numero != 0:
        aux = divmod(numero,10)
        numero = aux[0]
        sumDigit += aux[1]
    return sumDigit

def get_prime_numbers(num):
    numeros = list(range(2, num+1))
    for i in range(2, math.floor(math.sqrt(num))+1):
        if (numeros[i-2] != 0):
            for j in range(i, (math.floor(num/i)+1)):
                    numeros[i*j-2] = 0

    return numeros


array = [int(j) for j in input().split()]
primeNumbers = get_prime_numbers(suma_de_digitos(array[1]))
countPrimeNumbers = 0 
for i in range(2,(array[1]//array[2])+1):
    if (suma_de_digitos(array[2]*i) in primeNumbers):
        countPrimeNumbers+=1

print(countPrimeNumbers)
    
    
