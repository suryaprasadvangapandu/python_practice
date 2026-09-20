'''1. WAP to generate the Fibonacci series in between a range by dynamic inputs
   Ex: (W/O using built-in functions)
   begin = 4
   end = 15
   OP : [5, 8, 13]'''

# begin = int(input("Enter the begin value : "))
# end = int(input("Enter the end value : "))

# a = 0
# b = 1

# while a <= end:
#     if a >= begin:
#         print(a, end=" ")
    
#     c = a + b
#     a = b
#     b = c

'''2. WAP to check whether a number is a Palindrome or not (W/O using built-in functions)'''
# num= 122
# temp = num
# rev = 0
# while(num>0):
#     rem = num%10
#     rev = rev*10 +rem
#     num = num//10
# if(temp == rev):
#     print(f"{temp} is palindrome")
# else:
#     print(f"{temp} is not palindrome")

'''3. WAP to check whether a number is Magic Number or not (W/O using built-in functions)'''
# num = int(input("Enter the number : "))
# sum = 0
# sum1=0
# length = 0
# while(num>0):
#     rem=num%10
#     sum = sum+rem
#     num = num//10
# if(sum>9):
#     while(sum>0):
#         rem=sum%10
#         sum1 = sum1+rem
#         sum = sum//10
# if(sum1 == 1 or sum ==1 ):
#     print("Magic number")
# else:
#     print("Not a magic number")

'''4. WAP to store the factors of each number within a range by dictionary format
   Ex:     (W/O using built-in functions)
   begin = 5
   end = 9
   OP : 
   {5:[1,5], 6:[1,2,3,6], 7:[1,7], 8:[1,2,4,8], 9:[1,3,9]}'''

# begin = 5
# end = 9
# d1={}
# for i in range(begin,end+1):
#     l1=[]
#     for f in range(1,i+1):
#         if(i%f==0):
#             l1=l1+[f]
#     d1[i]=l1
# print(d1)

'''5. WAP to store the factorial of each number within a range by dictionary format
   Ex:     (W/O using built-in functions)
   begin = 2
   end = 6
   OP : {2:2, 3:6, 4:24, 5:120, 6:720}'''

# begin = 2
# end = 6
# d1={}
# for i in range(begin,end+1):
#     mul = 1
#     for f in range(1,i+1):
#         mul = mul*f
#     d1[i]=mul

# print(d1)

'''6. WAP to store the palindrome numbers in between a range within list format
   Ex       (W/O using built-in functions)
   begin = 100
   end = 140
   OP : [101, 111, 121, 131]'''

# begin = 100
# end = 140
# l1=[]
# for i in range(begin,end+1):
#     add=0
#     num =i
#     while(i>0):
#         rem = i%10
#         add = add*10+rem
#         i=i//10
#     if(num==add):
#         l1=l1+[num]

# print(l1)


'''7. WAP to generate the Armstrong numbers in between a range within list format
   Ex      (W/O using built-in functions)
   begin = 100
   end = 500
   OP :  [153, 370, 371]
'''

# begin = 100
# end = 500
# l1=[]
# for i in range(begin,end+1):
#     num1=i
#     num2=i
#     length = 0
#     add=0
#     while(i>0):
#         rem=i%10
#         length = length + 1
#         i=i//10
#     while(num1>0):
#         rem = num1%10
#         add = add+ rem**length
#         num1=num1//10
#     if(add ==num2):
#         l1 = l1+[num2]
        
# print(l1)
