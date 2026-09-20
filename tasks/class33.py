'''--task1--
1. WAP to check whether a number is an Abundant Number or not.
'''

# num = int(input("Enter the number for checking whether it is an Abundant Number or not: "))
# sum = 0
# for i in range(1, num):
#     if(num % i == 0):
#         sum += i

# if (sum > num):
#     print("Abundant Number")
# else:
#     print("Not an Abundant Number")

'''--task-2--
WAP to check whether a number is Strong Number or not.'''

# num = int(input("Enter the number for checking whether it is an Strong Number or not: "))
# sum = 0

# for dig in str(num):
#     factorial=1
#     for fac in range(1,int(dig)+1):
#         factorial = factorial*fac
#     sum = sum + factorial

# print(sum)

# if(sum==num):
#     print(f"{num} is an Strong number")
# else:
#     print(f"{num} is not an Strong number")

'''--task3--
WAP to check whether two numbers are friendly pair or not.
'''

# num1 = int(input("Enter the first number :"))
# num2 = int(input("Enter the Second number :"))
# sum1=0
# sum2=0

# for i in range(1,num1):
#     if(num1%i==0):
#         sum1+=i

# for i in range(1,num2):
#     if(num2%i==0):
#         sum2+=i

# if(sum1/num1 ==sum2/num2):
#     print("the two numbers are friendly pair")
# else:
#     print("the two numbers not  are friendly pair")

'''--task4--
WAP to check whether a number is a Composite Number or not.'''

# num = int(input("Enter the number : "))
# count=0
# for i in range(1,num+1):
#     if(num%i==0):
#         count+=1
# if(count > 2):
#     print(f"{num} is a composite number")
# else:
#     print(f"{num} is a not composite number")

'''task-5
WAP to check whether a number is an Automorphic Number or not.'''

# num = int(input("Enter the number : "))
# square = num**2
# length = len(str(num))
# rem = square%(10**length)
# if(num == rem):
#     print("Autpmorphic number")
# else:
#     print("Not an Autpmorphic number")


'''--task-6--
WAP to generate the Fibonacci Series upto n numbers.
   EX:
   n = 8
   0 1 1 2 3 5 8 13'''

# num = int(input("Enter the number : "))
# a=0
# b=1
# for i in range(num):
#     print(a,end=" ")
#     c= a+b
#     a=b
#     b=c


'''--task-7--
WAP to check whether a number is a Harshad Number or not.'''

# num= int(input("Enter the number : "))
# sum = 0
# for dig in str(num):
#     sum = sum+int(dig)

# if(num%sum==0):
#     print("harshad Number")
# else:
#     print("Not Harshad Number")

'''--task-8--
WAP to perform total sum of digits exists in a string.
   EX: sentence = "Raju worked for 3 days to earn Rs.17,585.12/-"
   OP : 32'''

# sentence = input("Enter the sentence :")
# sum = 0
# for dig in sentence:
#     if(dig.isdigit()):
#         sum = sum + int(dig)

# print("the sum of the digits in sentence is :",sum)
