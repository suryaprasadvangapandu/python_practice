'''1. WAP to findout the factors of a number'''

# num = 12
# i=1
# while(i<=num):
#     if(num%i==0):
#         print(i)
#     i+=1

'''2.WAP to findout the factorial of a number''' 
# num = 4
# fact=1
# i=1
# while(i<=num):
#     fact=fact*i
#     i+=1
# print(fact)


'''3. WAP to check whether a number is a Armstrong number of not (W/O using built-in func)'''

# num1 = 170
# num2 = num1
# num3 = num1
# count = 0
# sum = 0
# while(num1>0):
#     num1 = num1//10
#     count+=1
# while(num2>0):
#     rem = num2%10
#     sum = sum +rem**count
#     num2= num2//10
# if(num3 == sum ):
#     print(f"{num3} is an palindrome number ")
# else:
#     print(f"{num3} is not a palindrome number ")


'''4. WAP to findout the length of an integer  (W/O using built-in func)'''

# num = 1450
# temp = num
# count = 0
# while(num>0):
#     num = num//10
#     count+=1
# print(f"count of {temp} is : {count}")

'''5. WAP to check whether a number is a Perfect Number or not'''

# num = 14
# temp = num
# i=1
# sum =0
# while(i<num):
#     if(num%i==0):
#         sum = sum + i
#     i+=1
# if(sum == temp ):
#     print(f"{temp} is perfect number")
# else:
#     print(f"{temp} is not an prefect number")