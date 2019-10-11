testCases = int(input())
for i in range(testCases):
    array = [int(j) for j in input().split()]
    botellas = 0
    result = 0 
    while(array[0] >= array[1] ):
        result = divmod(array[0],array[1])
        botellas+=result[0]
        array[0] = result[0]+result[1]
    
    print(botellas)
    