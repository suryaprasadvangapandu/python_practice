'''1. WAP to the perform alternative of split() without using any built-in functions as follows :
Ex: Role = “Django-Flask-Developer” Sep = “-“ 
Output : [‘Django’, ‘Flask’, ‘Developer’] '''

# num = "Django-Flask-Developer"

# l1 = []
# sep = "-"
# add = ""

# for i in num:   
#   if (i!=sep):
#        add = add + i
#   else:
#       l1+=[add]
#       add = ""

# l1+=[add]

# print(l1)


'''
2. WAP to perform the Factors of Palindrome Numbers in the list without using any built-in functions.
Ex : Nums = [787, 5445, 672, 67, 343] 
# Output : { 787 : [1, 787], 5445 : [1, 3, 5, 9, 11, 15, 33, 45, 55, 99, 121, 165, 363, 495, 605, 1089, 1815, 5445], 343 : [1, 7, 49, 343] } '''


# nums = [787, 5445, 672, 67, 343]

# d1 = {}

# for i in nums:

#     add = 0
#     temp = i

#     while i > 0:
#         rem = i % 10
#         add = add * 10 + rem
#         i = i // 10

#     if add == temp:
#         l1 = []

#         for j in range(1, temp + 1):
#             if temp % j == 0:
#                 l1 += [j]

#         d1[temp] = l1

# print(d1)



'''3. WAP to find all pairs of numbers in a list that sum to a given target value.
Ex : Nums = [2, 4, 3, 5, 6] 
target = 7 
Output: [(2, 5), (4, 3)]''' 

# l1 = []
# nums = [2, 4, 3, 5, 6]
# target = 7
# for i in range(len(nums)):
#      for j in range(i+1,len(nums)):
#          if(nums[i] + nums[j] == target):
#                 l1.append((nums[i],nums[j]))
# print(l1)


'''4. WAP to check whether the list is containing only palindrome Numbers or not. 
Ex : Nums1 = [23, 454, 898, 34, 23432] #False 
Nums1 = [767, 78687, 8998, 25452, 111] #True '''
   
# nums = [767, 78687, 8998, 25452, 111]
# flag = True
# for i in nums:
#     add = 0
#     temp = i
#     while(i>0):
#       rem= i%10
#       add = add*10+rem
#       i = i//10
#     if(add !=temp):
#           flag = False
#           break
# if(flag):
#   print("True")
# else:
#   print("False")


'''5. WAP to generate Magic Numbers in between begin and end dynamic inputs by using while loop only and store all Magic Numbers in a list '''

# begin = int(input("Enter the begin number: "))
# end = int(input("Enter the end number: "))

# l1 = []

# while begin <= end:

#     temp = begin
#     num = begin

#     while num > 9:
#         add = 0 

#         while num > 0:
#             rem = num % 10
#             add = add + rem
#             num = num // 10

#         num = add

#     if num == 1:
#         l1 += [temp]

#     begin = begin + 1

# print(l1)   



'''6. If nums = [[1, 2], [3, 4], [5, 6]] then show output as follows by using List Comprehension. 
Output : [[1, 3, 5], [2, 4, 6]] '''

# nums = [[1, 2], [3, 4], [5, 6]]
# l1 = [[ nums[j][i] for j in range(len(nums))]for i in range(len(nums[0]))]
# print(l1)


'''7. Flatten the list nums = [[1, 2], [3, 4], 5, [6, 7]] using List Comprehension.
OUTPUT : [1, 2, 3, 4, 5, 6, 7]'''

# nums = [[1, 2], [3, 4], 5, [6, 7]]
# l1 = [j for i in nums for j in (i if(type(i) == list) else [i])]
# print(l1)


'''8. Ignore the digits from the list mat = [['a', '1', 'b'], ['2', 'c', '3'], ['5’, 'e', '8']] and Create a New List as follows :'
OUTPUT : [['a', 'b'], ['c'], ['e']] '''
                 
         
# mat = [['a', '1', 'b'], ['2', 'c', '3'], ['5', 'e', '8']]

# l1 = []

# for i in mat:
#     l2 = []

#     for j in i:
#         if ('a' <= j <= 'z'):
#             l2 += [j]

#     l1 += [l2]

# print(l1)

