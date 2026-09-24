'''1. WAP to get list of Automorphic Numbers in between a range by using List Comprehension.'''

# begin = 1 
# end = 10

# l1 = [i for i in range(begin, end) if i ** 2 % (10 ** len(str(i))) == i]

# print(l1)

'''2. WAP to get the factors of a number'''
# num = 7
# l1 = [ i for i in range(1,num+1) if(num%i==0)]
# print(l1)

'''3. WAP to get list of Harshad Numbers in between a range by List Comprehension.'''
# begin = 1
# end =10
# l1 =[i for i in range(begin,end+1)  if i % sum(int(j) for j in str(i))==0]
# print(l1)


'''4. WAP to get list of Perfect Numbers in between a range by using List Comprehension.'''
# begin = 1
# end = 10
# l1 = [i for i in range(begin,end+1) if sum(j for j in range(1,i) if(i%j == 0))== i]
# print(l1)

'''5. Create the below list by comprehension if num=5
   [1, 22, 333, 4444, 55555]'''
# num = 5
# l1 = [f"{str(i)*i}" for i in range(1,num+1) for j in range(1)]
# print(l1)

'''6. Create the below list by comprehension 
   if num=3
   [[1,2,3], [4,5,6], [7,8,9]]'''

# num = 3
# l1 = [[j+(num*i) for j in range(1,num+1)] for i in range(0,num)]
# print(l1)


'''6. Create the below list by comprehension 
if num=4
   [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]'''
# num = 4
# l1 = [[j+(num*i) for j in range(1,num+1)] for i in range(0,num)]
# print(l1)


