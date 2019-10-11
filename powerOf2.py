numOfTest = int(input())
counter = 0
for i in range(0,numOfTest):
    num = int(input())
    prueba = num & (num-1)
    if (prueba==0):
        counter +=1

print(counter)