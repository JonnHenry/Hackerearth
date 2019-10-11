'''
Subham is a very irritating guy. He loves to pester people to their fullest. All the teachers are quite frustrated with him. Even his friends get sometimes frustrated with his constant naggings.

So, one fine day, Shubham was testing his “talent” on our very beloved friend Tuhin!! Being a short-tempered guy, Tuhin quickly got pissed off. So, he decided to teach him a lesson.

He gave him a string of length N, more precisely a “binary string”, consisting of only 0’s and 1’s. He asked him to find all the strings generated from N left rotations one character at a time. For example if S is "101", then the strings generated from left rotations will be “011”, ”110” and ”101”. Out of the generated N strings, he asks the number of strings having even decimal value.

Help Subham to solve this problem
'''
numCasesOfTest = int(input())
for i in range(0,numCasesOfTest):
    numBits = int(input())
    print(input().count('0'))
    