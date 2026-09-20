'''num =5
for i in range(1,num+1):
    for space in range(num-i):
        print(" ",end="")
    for j in range(0,i):
        print(i,end=" ")
    print()

    1 
   2 2 
  3 3 3 
 4 4 4 4 
5 5 5 5 5 '''

'''num = 5
for i in range(1,num+1):
    for  j in range(i-1):
        print(" ",end="")
    for j in range(num+1-i):
        print(i,end=" ")
    print()


1 1 1 1 1 
 2 2 2 2 
  3 3 3 
   4 4 
    5 '''

'''num = 5
for i in range(1,num+1):
    for  j in range(i-1):
        print(" ",end="")
    for j in range(1,num+2-i):
        print(j,end=" ")
    print()


1 2 3 4 5 
 1 2 3 4 
  1 2 3 
   1 2 
    1 
'''

'''num = 5
for i in range(1,num+1):
    for  j in range(i-1):
        print(" ",end="")
    for j in range(num+1-i,0,-1):
        print(j,end=" ")
    print()


5 4 3 2 1 
 4 3 2 1 
  3 2 1 
   2 1 
    1 '''

'''num = 5
for i in range(num,0,-1):
    for  j in range(i-1):
        print(" ",end="")
    for j in range(num-i+1):
        print(i,end=" ")
    print()

    5 
   4 4 
  3 3 3 
 2 2 2 2 
1 1 1 1 1 '''



'''num =4
for i in range(65,65+num):
    for j in range(1,num+1):
        print(chr(i),end=" ")
    print()

A A A A 
B B B B 
C C C C 
D D D D '''


'''num =4
for i in range(1,num+1):
    for j in range(65,65+num):
        print(chr(j),end=" ")
    print()

A B C D
A B C D
A B C D
A B C D '''




'''num=4
for i in range(num,0,-1):
    for j in range(num-i):
        print("*",end="")
    for j in range(i):
        print(chr(i+64),end=" ")
    print()

D D D D 
*C C C 
**B B 
***A '''


'''num =4
for i in range(1,num+1):
    for j in range(num-i):
        print("*",end="")
    for j in range(i):
        print(chr(i+64),end=" ")
    print()

***A 
**B B 
*C C C 
D D D D '''