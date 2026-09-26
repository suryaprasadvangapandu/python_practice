'''1) Input:
   a = [1, 2, 3]
   b = [4, 5]

   Output: [(1,4), (1,5), (2,4), (2,5), (3,4), (3,5)]'''

# a = [1, 2, 3]
# b = [4, 5]
# l1 =[(i,j) for i in a for j in b]
# print(l1)
        

'''2) From 1 to 100, create a new list containing squares of only even numbers'''
# end = 100
# l1 = [i**2 for i in range(1,end+1) if(i%2==0)]
# print(l1)

'''3) From a list of names, create a dictionary where:
   key = name
   value = length of name'''

# names = ["Ravi", "Suresh", "Prakash", "Kiran", "Arjun", "Rahul", "Vijay", "Ajay", "Ramesh", "Sai"]
# l1 = [{i:len(i)}for i in names]
# print(l1)

'''4) Find all numbers between 1 and 100 that are divisible by 2, 3, and 5.'''
# end = 100
# l1 = [i for i in range(1,end+1) if(i%2 == 0 and i%3==0 and i%5==0)]
# print(l1)


'''5) numbers = [10, 15, 10, 20, 25, 15, 30, 35, 20, 40]

   Using set comprehension, create a set containing numbers that are:
   unique
   divisible by 5
   greater than 15'''

# numbers = [10, 15, 10, 20, 25, 15, 30, 35, 20, 40]
# s1 = {i for i in numbers if(i%5==0 and i>15)}
# print(s1)


'''6) text = "Python Programming 2026"

   Using comprehension, create:

   A. A list of all vowels
   B. A list of all consonants
   C. A list of all digits
   D. A list of all uppercase characters
   E. A list of all characters excluding spaces'''

# text = "Python Programming 2026"
# l1 = [i for i in text if(i in "AEIOUaeiou")]
# print(l1)
# l2 = [i for i in text if(i not in "AEIOUaeiou" and i.isalpha())]
# print(l2)
# l3 = [i for i in text if(i.isdigit())]
# print(l3)
# l4 = [i for i in text if(i == i.upper() and i != " " and i.isalpha())]
# print(l4)
# l5 = [i for i in text if(i.isalpha() or i == " ")]
# print(l5)


'''7) Input:
   data = [
       [10, 15, 20],
       [25, 30, 35],
       [40, 45, 50]
   ]
   Output:
   [10, 20, 30, 40, 50]'''

# data = [[10, 15, 20],[25, 30, 35],[40, 45, 50]]
# l1 = [j for i in data for j in i if(j%10 == 0)]
# print(l1)
