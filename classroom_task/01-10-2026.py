'''1.Create a Function to check whether a number is even or not.'''
# def isEven(num):
#         return num%2==0
# print(isEven(2))


'''2.Create a Function to check whether a number is odd or not.'''

# def isOdd(num):
#         return num%2==1
# print(isOdd(2))

'''3.Create a Function to check whether a number is even number or odd number.'''
# def is_Even_or_Odd(num):
#     if(num%2==1):
#         return "Odd Number"
#     else:
#         if(num==0):
#             return "Neutral"
#         else:
#             return "Even Number"

# print(is_Even_or_Odd(3))

'''4.Create a Function to generate & store even numbers in list format based on start and stop input provided by user.'''

# def even(start,stop):
        
#         def isEven(num):
#                 return num%2==0
#         l1=[]
#         for i in range(start,stop):
#                 if(isEven(i)):
#                         l1.append(i)
#         return l1

# start = int(input("Enter the start point:"))
# stop= int(input("Enter the end point:"))
# print(even(start,stop))

'''5.Create a Function to check whether a number is Prime Number or not.'''
# def isprime(num):
#     count = 0
#     for i in range(1,num+1):
#         if(num%i==0):
#             count +=1
#     if(count == 2):
#         return "Prime Number"
#     else:
#         return "Not Prime Number"
# print(isprime(4))


'''6.Create a Function to generate & store prime numbers in list format based on start and stop input provided by user'''


# def prime(start,stop):
#     def isprime(num):
#         count = 0
#         for i in range(1,num+1):
#             if(num%i==0):
#                 count +=1
#         return count == 2
#     l1 = []
#     for i in range(start,stop):
#         if(isprime(i)):
#             l1.append(i)
#     return l1

# start = int(input("Enter the start number : "))
# stop = int(input("Enter the stop number : "))
# print(prime(start,stop))


'''7.Create a Function to check whether a number is Composite Number or not.'''

# def isComposite(num):
#     count = 0
#     for i in range(1,num+1):
#         if(num%i==0):
#             count +=1
#     if(count >2):
#         return "Composite Number"
#     else:
#         return "Not Composite Number"
# print(isComposite(6))

'''8.Create a Function to generate & store Composite Numbers in list format based on start and stop input provided by user'''

# def composite(start,stop):
#     def isComposite(num):
#         count = 0
#         for i in range(1,num+1):
#             if(num%i==0):
#                 count +=1
#         return count > 2
#     l1 = []
#     for i in range(start,stop):
#         if(isComposite(i)):
#             l1.append(i)
#     return l1

# start = int(input("Enter the start number : "))
# stop = int(input("Enter the stop number : "))
# print(composite(start,stop))


'''9.Create a Function to check whether a number is Armstrong Number or not.'''

# def isArmstrong(num):
#     def length(lth):
#         count = 0
#         while(lth>0):
#             lth = lth//10
#             count+=1
#         return count
    
#     temp = num
#     sum = 0
#     while(temp >0):
#         rem = temp%10
#         sum = sum+rem**length(num)
#         temp = temp//10
#     if(sum == num):
#         return "Armstrong Number"
#     else:
#         return "Not Armstrong Number"

# print(isArmstrong(153))


'''10.Create a Function to generate & store Armstrong Numbers in list format based on start and stop input provided by user.'''

# def Armstrong(start,stop):
#     def isArmstrong(num):
#         def length(lth):
#             count = 0
#             while(lth>0):
#                 lth = lth//10
#                 count+=1
#             return count
    
#         temp = num
#         sum = 0
#         while(temp >0):
#             rem = temp%10
#             sum = sum+rem**length(num)
#             temp = temp//10
#         return sum == num
#     l1 = []
#     for i in range(start,stop):
#         if(isArmstrong(i)):
#             l1.append(i)
#     return l1

# start = int(input("Enter the start number : "))
# stop = int(input("Enter the stop number : "))
# print(Armstrong(start,stop))

'''11.Create a Function to check whether a number is Perfect Number or not.'''

# def isPerfect(num):
#     sum =0
#     for i in range(1,num):
#         if(num%i==0):
#             sum += i
#     return sum == num

# print(isPerfect(2))

'''12.Create a Function to check whether a number is Strong Number or not.'''

# def isStrong(num):
#     def factorial(ftrl):
#         fact = 1
#         for i in range(1,ftrl+1):
#             fact *= i
#         return fact
#     temp = num
#     sum = 0
#     while(temp>0):
#         rem = temp%10
#         sum = sum+factorial(rem)
#         temp = temp//10
#     return sum == num

# print(isStrong(3))

'''13.Create a Function to check whether a number is Harshad Number or not.'''

# def isHarshad(num):
#     temp = num
#     sum = 0
#     while(temp>0):
#         rem = temp%10
#         sum = sum+rem
#         temp = temp//10
#     return num%sum == 0

# print(isHarshad(21))

# '''14.Create a Function to check whether a number is Abundant Number or not.'''
# def isAbundant(num):
#     sum = 0
#     for i in range(1,num):
#         if(num%i==0):
#             sum = sum+i
#     return sum> num

# print(isAbundant(18))

'''15.Create a Function to check whether a number is Automorphic Number or not.'''
# def isAutomorphic(num):
#     def length(lth):
#             count = 0
#             while(lth>0):
#                 lth = lth//10
#                 count+=1
#             return count
#     if((num**2)%10**length(num)== num):
#         return "Automorphic Number"
#     else:
#         return "Not Automorphic Number"

# print(isAutomorphic(12))

'''16.Create a Function to find the factorial of a number'''

# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact = fact*i
#     return fact
# print(factorial(5))



'''17.Create a Function to find the factorial of each number in between range provided by user and stores them in dictionary format where key is each number and value is its respective factorial value.'''

# def factorialRange(start,stop):
#     d1={}
#     def factorial(num):
#         fact=1
#         for i in range(1,num+1):
#             fact = fact*i
#         return fact
#     for i in range(start,stop):
#         d1[i]=factorial(i)
#     return d1
# start = int(input("Enter the start number : "))
# stop = int(input("Enter the stop number : "))
# print(factorialRange(start,stop))

'''18.Create a Function to find the factors of a number.'''

# def factors(num):
#     l1=[]
#     for i in range(1,num+1):
#         if(num%i==0):
#             print(i)

# factors(6)


'''19.Create a Function to find the factors of each number in between range provided by user and stores them in dictionary format where key is each number and value is its respective factors in list format'''
# def factRange(start,stop):
#     def factors(num):
#         d1={}
#         l1=[]
#         for i in range(1,num+1):
#             if(num%i==0):
#                 l1.append(i)
#             d1[num] = l1
#         return d1
#     for i in range(start,stop):
#         print(factors(i))

# start = int(input("Enter the start number : "))
# stop = int(input("Enter the stop number : "))
# factRange(start,stop)

'''20.Create a Function to check whether a number is Magic Number or not.'''

# def MagicNumber(num):
#     while(num>9):
#         sum=0
#         while(num>0):
#             rem = num%10
#             sum = sum+rem
#             num=num//10
#         num = sum
#     return num == 1
# print(MagicNumber(10))
