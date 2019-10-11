numOfData = int(input())
arrayBinary = [int(j) for j in input().split()]
contIndex = 0
suma = 0
position = 0
contBinary = 0

while(contIndex <= numOfData-1):
    if (arrayBinary[contIndex] == 1):
        if (arrayBinary[numOfData-(1+contBinary)] != 1):
            arrayBinary[contIndex] = 0
            arrayBinary[numOfData-(1+contBinary)] = 1
            break
        else:
            contBinary += 1
        if (contBinary > numOfData or contIndex == numOfData-1):
            break

    else:
        contIndex += 1
        contBinary = 0


for i in arrayBinary:
    if (i != 0):
        suma += (2**position)
    else:
        position += 1


print(suma)
