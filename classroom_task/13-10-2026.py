'''-----PART-1----------'''
'''1. Write a Python program to generate *10 random integers* between 1 and 100.'''
# import random
# for i in range(10):
#     print(f" random integers between 1 and 100 is {random.randint(1,100)}")

'''Write a Python program to generate *15 random integers* between 10 and 500.'''
# import random
# for i in range(15):
#     print(f" random integers between 1 and 100 is {random.randint(10,500)}")

'''Write a Python program to generate *7 random numbers* between user-provided beginning and ending values.'''
# import random
# begin = int(input("Enter the begin number : "))
# end = int(input("Enter the end number : "))
# for i in range(7):
#     print(f" random integers between 1 and 100 is {random.randint(begin,end)}")

'''Write a Python program to generate *10 random even numbers* between 1 and 100.'''
# import random

# for i in range(10):
#     num = random.randint(1, 100)

#     while num % 2 != 0:
#         num = random.randint(1, 100)

#     print(f"Random even number is {num}")

'''Write a Python program to generate *10 random odd numbers* between 1 and 100.'''
# import random

# for i in range(10):
#     num = random.randint(1, 100)

#     while num % 2 == 0:
#         num = random.randint(1, 100)

#     print(f"Random odd number is {num}")


'''Write a Python program to generate *5 random multiples of 5* between 1 and 500.'''
# import random

# for i in range(5):
#     num = random.randint(1, 500)

#     while num % 5 != 0:
#         num = random.randint(1, 500)

#     print(f"Random odd number is {num}")

'''Write a Python program to generate *10 random numbers* between 100 and 999'''
# import random
# for i in range(10):
#     print(f" random integers between 1 and 100 is {random.randint(100,999)}")

'''Write a Python program to generate *10 random floating-point numbers* between 1 and 50.'''
# import random
# for i in range(10):
#     print(f" random integers between 1 and 100 is {random.uniform(1,50)}")


'''Write a Python program to generate *7 random floating-point numbers* 
between user-provided beginning and ending values, with *2 decimal places'''
# import random
# begin = int(input("Enter the begin number : "))
# end = int(input("Enter the end number : "))
# for i in range(7):
#     print(f" random integers between 1 and 100 is {round(random.uniform(begin,end),2)}")

'''Write a Python program to generate *10 random floating-point numbers* between 10 and 100, with *4 decimal places*.'''
# import random
# for i in range(10):
#     print(f" random integers between 1 and 100 is {round(random.uniform(10,100),4)}")

'''-----PART-2----------'''
'''11. Write a Python program to generate *10 random Indian mobile numbers* containing exactly 10 digits.'''
# import random
# for i in range(10):
#     print(f"Indian mobile numbers* containing exactly 10 digits is +91 {random.randrange(6000000000,10000000000)}")

'''Write a Python program to generate *15 random Indian mobile numbers*, with each number starting with 6, 7, 8, or 9.'''
# import random
# for i in range(10):
#     print(f"Indian mobile numbers* containing exactly 10 digits is +91 {random.randrange(6000000000,10000000000)}")


'''Write a Python program to generate *5 random mobile numbers* starting with 9.'''
# import random
# for i in range(10):
#     print(f"Indian mobile numbers* containing exactly 10 digits is +91 {random.randrange(9000000000,10000000000)}")

'''Write a Python program to generate *10 random mobile numbers* starting with 8.'''
# import random
# for i in range(10):
#     print(f"Indian mobile numbers* containing exactly 10 digits is +91 {random.randrange(8000000000,9000000000)}")