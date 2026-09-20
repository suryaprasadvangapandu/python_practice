'''1.Write a Python Program to retrieve the Leap Years only from the list and stores them 
in tuple format. 
Ex : Years = [2000, ‘2012’ 1976, 1826, 1732]
 Output : (2000, 1976, 1732) 
 '''

# years = [2000, '2012', 1976, 1826, 1732]

# l1 = ()

# for i in years:
#     if i == int(i):
#         if i % 400 == 0 or (i % 4 == 0 and i % 100 != 0):
#             l1 = l1+(i,)
# print(l1)


'''2. Write a Python Program to retrieve the Palindrome Strings Only from the tuple without using Slicing Operator.
Ex : Elements = (“RIMJIM”, “RACECAR”, “NANDAN”, “RACER”) 
 Output : [“RACECAR”] '''

# Elements = ("RIMJIM", "RACECAR", "NANDAN", "RACER")
# l1 = []
# for word in Elements:
#     add=""
#     for c in word:
#         add = c +add
#     if(add == word):
#         l1=l1+[word]
# print(l1)


'''3. Write a Python Program to find the Prime Factors of a Number. 
Ex: Num = 15
Output : Prime Factors of 15 : [3, 5] '''

# num = 6
# l1= []
# l2= []
# for i in range(1,num):
#     if(num % i ==0):
#         l1 = l1+[i]

# for i in l1:
#     count = 0
#     for p in range(1,i+1):
#         if(i%p==0):
#             count += 1
#     if(count ==2):
#         l2=l2+[i]
# print(l2)


'''4. Write a Python Program to perform alternate of upper() without using any builtin functions as follows : 
Ex : Cafe = “Ni-Loufer” 
Output : ‘NI-LOUFER’ '''


# cafe = "Ni-Loufer"
# result =""
# for  ch in cafe:
#     if('a'<= ch <= 'z'):
#         result= result+chr(ord(ch)-32)
#     else:
#         result= result+ch
# print(result)


'''5. Write a Python Program to perform alternate of swapcase() without using any built-in functions as follows : 
Ex : Actor = “SaMPooRnESH” 
Output : ‘sAmpOOrNesh’ '''

# Actor = "sAmpOOrNesh"
# result =""
# for  ch in Actor:
#     if('a'<= ch <= 'z'):
#         result= result+chr(ord(ch)-32)
#     elif('A' <= ch <= 'Z'):
#         result= result+chr(ord(ch)+32)
#     else:
#         result= result+ch
# print(result)


'''6. Write a Python Program to perform to the alternate of isdigit() without using any built-in functions as follows :
Ex : Storage = “64GB”  #False
Date = “June21” #False 
Pos_Integer = “54262” #True
Neg_Integer = “-45” #False 
Float = “90.34” #False '''


# Storage = "64GB" 
# Date = "June21"
# Pos_Integer = "54262" 
# Neg_Integer = "-45"
# Float = "90.34"


# d1= {}
# d1.update({"storage":"64GB","Date":"June21","Pos_Integer" : "54262","Neg_Integer" : "-45","Float" : "90.34"})

# for i in d1:
#     count=0
#     for ch in d1[i]:
#         if('0' <= ch <= '9'):
#             count=1
#         else:
#             count=0
#             break
#     if(count==1):
#         print(f"{d1[i]}--> True")
#     else:
#         print(f"{d1[i]}-->False")
    
            
            
'''
7. Write a Python Program to Perform Numbers into English Format without using built-in functions.
Ex : Num = 65689 
Output : Six Five Six Eight Nine'''

# d1={}
# num = 65689
# d1[1] = "ONE"
# d1[2] ="TWO"
# d1[3]="THREE"
# d1[4]="FOUR"
# d1[5]="FIVE"
# d1[6]="SIX"
# d1[7]="SEVEN"
# d1[8]="EIGHT"
# d1[9]="NINE"
# d1[0]="ZERO"

# add=""

# while(num>0):
#     rem= num%10
#     add = d1[rem]+" "+add
#     num=num//10

# print(add)


'''8. Write a Python Program to check whether the list is containing only palindrome Numbers or not. 
Ex : Nums1 = [23, 454, 898, 34, 23432] #False 
Nums1 = [767, 78687, 8998, 25452, 111] #True '''

# Nums1 = [767, 78687, 8998, 25452, 111]

# for i in Nums1:
#     num = i
#     add = 0

#     while(i > 0):
#         rem = i % 10
#         add = add * 10 + rem
#         i = i // 10

#     if(add != num):
#         print("False")
#         break
# else:
#     print("True")


'''9. Write a Python Program to display the Factors of every Positive Number in the dict format
Ex : Nums = [3, 9, -31 8, 0 14, 11] 
Output : {3:[1, 3], 9:[1, 3, 9], 8:[1, 2, 4, 8], 14:[1, 2, 7, 14], 11:[1, 11]}'''


# Nums = [3, 9, -31, 8, 0 ,14, 11]
# d1={}
# for i in Nums:
#     if(i>0):
#         l1=[]
#         for f in range(1,i+1):
#             if(i%f==0):
#                 l1.append(f)
#         d1[i]=l1
# print(d1)


'''10. Write a Python Program ➢ to Check Whether the Number is Spy Number or not. 
Ex : Num1 = 123 Num2 = 112 
Output: 123 is Spy Number 112 is not Spy Number 
NOTE : Sum of digits equals product of digits.
{ 1+2+3 = 6 1x2x3 = 6 So 123 is Spy Number}'''

# num = 133
# add=0
# mul=1
# while(num>0):
#     rem = num%10
#     add = add+rem
#     mul = mul*rem
#     num=num//10
# if(add==mul):
#     print("spy number")
# else:
#     print("Not spy number")


'''11. to check whether the Number is a Special Number or not. 
Ex : Num1 = 12 Num2 = 13 
Output : 12 is a Special Number (Krishnamurthy Number) 13 is not a Special Number 
NOTE : Special Number refers to the Sum of factorial of digits of the number is equal to sum of the digits 
{1! +2! = 3 1 + 2 = 3 So 12 is Special Number}'''


# num = 12
# temp = num
# add1=0
# add2=0

# while(num>0):
#     rem = num%10
#     add1 = add1+rem
#     num = num//10

# while(temp>0):
#     rem = temp%10
#     fact = 1
#     for i in range(1,rem+1):
#         fact = fact*i
#     add2 = add2 +fact
#     temp = temp//10
# if(add1==add2):
#     print("Special Number")
# else:
#     print("Not a Special Number")