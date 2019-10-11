'''
In the world of dragon ball, Goku has been the greatest rival of Vegeta. 
Vegeta wants to surpass goku but never succeeds. 
Now that he knows he cant beat goku in physical strength, he wants to be satisfied by beating goku in mental strength. 
He gives certain inputs and outputs , Goku needs to find the logic and predict the output for the next inputs. 
Goku is struggling with the challenge, your task is to find the logic and and help him win the challenge.

INPUT :

Given a series of numbers(inputs) and each number(N) on a newline.

OUTPUT :

For the given input , Output the required ans.
'''

while(True):
    try:
        print(bin(int(input())).count('1'))
    except EOFError:
        break