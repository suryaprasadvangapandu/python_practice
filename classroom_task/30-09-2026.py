'''prime number using function'''

# def is_prime(num):
#     if(num<2):
#         return False
#     for i in range(2,num):
#         if(num%i==0):
#             return False
#     else:
#         return True
# for i in range(1,10):
#     if(is_prime(i)):
#         print(i)
        
'''factorial using function'''

# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact = fact*i
#     return fact



# for i in range(1,10):
#     print(factorial(i))

'''factors using function'''
# def factors(num):
#     d1={}
#     l1=[]
#     for i in range(1,num+1):
#         if(num%i==0):
#             l1.append(i)
#         d1[num] = l1
#     return d1


# for i in range(1,10):
#     print(factors(i))


'''palindrome using function'''

# def palindrome(num):
#     temp = num
#     rev=0
#     while(num>0):
#         rem = num%10
#         rev = rev*10+rem
#         num = num//10
#     if(rev == temp):
#         return True
#     else:
#         return False
# for i in range(1,1000+1):
#     if(palindrome(i)):
#         print(i)




