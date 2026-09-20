'''--task-1--
WAP to calculate the final bill amount after adding GST based on purchased amount.

  -> Add 5% GST, if purchased amount is less than 5000
  -> Add 8% GST, if purchased amount is more than 5000 and upto 15000
  -> Add 12% GST, if purchased amount is more than 15000 and upto 30000
  -> Add 18% GST, if purchased amount is more than 30000
'''

# purchased_amount = float(input("Enter the purchased amount: "))

# if(0 < purchased_amount < 5000):
#     gst = purchased_amount * (5 / 100)

# elif(5000 <= purchased_amount <= 15000):
#     gst = purchased_amount * (8 / 100)

# elif(15000 < purchased_amount <= 30000):
#     gst = purchased_amount * (12 / 100)

# else:
#     gst = purchased_amount * (18 / 100)

# final_amount = purchased_amount + gst

# print(f"GST amount is: {gst}")
# print(f"Final amount after adding GST is: {final_amount}")


'''
Task-2:
---------
WAP to display the content as below requirements.

 -> If a number is divisible by 3 then show as "Fizz"
 -> If a number is divisible by 5 then show as "Buzz"
 -> If a number is divisible by both 3 and 5 then show as "FizzBuzz"
'''
# num = int(input("Enter the number :"))
# if(num%3==0 and num%5==0):
#     print("FizzBuzz")
# elif(num%5==0):
#     print("Buzz")
# elif(num%3==0):
#     print("Fizz")

'''---task-3---
1. WAP to store Even Numbers in a list by taking begin and end as dynamic inputs.'''

# begin = int(input("Enter the begin value : "))
# end = int(input("Enter the end value: "))
# l1=[]
# for i in range(begin,end+1):
#     if(i%2==0 and i>0):
#         l1.append(i)
# print(f"list formed by containg the even numbers is : {l1}")


'''---task-4---
WAP to store Odd Numbers in a list by taking begin and end as dynamic inputs.'''

# begin = int(input("Enter the begin value : "))
# end = int(input("Enter the end value: "))
# l1=[]
# for i in range(begin,end+1):
#     if(i%2!=0 and i>0):
#         l1.append(i)
# print(f"list formed by containg the odd numbers is : {l1}")

'''--task-5--
WAP to findout the factors of a specific number and store factors in a list format.'''

# num = int(input("Enter the number that used for finding the factor is :"))

# l1 = []
# for i in range(1,num+1):
#     if(num%i==0):
#         l1.append(i)
# print(f"{num}-->factors in the list is : {l1}")
