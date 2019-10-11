array = [int(j) for j in input().split()]
lostAll = array[0]//array[2]
bobHave = lostAll * array[3]+array[1]
print(bobHave)
