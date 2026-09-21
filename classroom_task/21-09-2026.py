'''1.prime number'''
# num = 5

# for i in range(2,num):
#     if(num%i==0):  
#         print( " not Prime number ")
#         break
# else:
#     print(" prime")


"""or""" 


# num= 10
# i=2
# while(i<num):
#     if(num%i==0):
#         print("Not prime")
#         break
#     i+=1
# else:
#     print("Prime")


'''2.composite number'''

# num = 6

# for i in range(2,num):
#     if(num%i==0):  
#         print( "composite number")
#         break
# else:
#     print(" prime")


"""or"""

# num= 10
# i=2
# while(i<num):
#     if(num%i==0):
#         print("composite number")
#         break
#     i+=1
# else:
#     print("Prime")


'''3.magic number using the while loop'''

# num =173
# add= 0
# while(num>9):
#     add=0
#     while(num>0):
#         rem = num%10
#         add = add+rem
#         num = num//10
#     num = add

# if(num == 1):
#     print("Magic number")
# else:
#     print("Not a Magic number")

'''4.display the 1000  range palindrome number'''
# l1=[]
# for num in range(1,1000+1):
        
#         temp = num
#         add=0
#         while(num>0):
#             rem = num%10
#             add = add*10+rem
#             num = num//10
#             if(temp == add):
#                 l1.append(add)
# print(l1)

'''5.display the 1000  range Amstrong number'''
# l1=[]

# for num in range(1,1000+1):
#         temp = num
#         num1=num
#         add=0
#         length = 0
#         while(num1>0):
#             rem = num1%10
#             length +=1
#             num1= num1//10
            
#         while(num>0):
#             rem = num%10
#             add = add+rem**length
#             num = num//10
#             if(temp == add):
#                 l1.append(add)
# print(l1)

'''6.Strong number'''
# l1=[]
# for num in range(1,1000+1):
#         add=0
#         temp =num
#         while(num>0):
#             rem = num%10
#             fact=1
#             for i in  range(1,rem+1):
#                 fact = fact*i
#             add = add+fact
#             num = num//10

#         if(temp == add):
#             l1.append(add)

# print(l1)


'''7.check two numbes are friendly pairs or not '''

# num1 = 6
# num2 = 2
# add1 = 0
# add2 = 0
# for i in range(1,num1):
#     if(num1%i==0):
#         add1= add1+i
# for i in range(1,num2):
#     if(num2%i==0):
#         add2 = add2+i

# if(add1/num1 == add2/num2):
#     print("Friendly pair")
# else:
#     print("Not a Friendly pair")    


'''8.find out the pairs whose addition of the two numbers in the pairs  are equal to target whose are matching with given targing '''
num = [1,7,4,2,3]
target = 5 

# for i in range(len(num)):
#     for j in range(len(num)):
#         if(num[i]+num[j]==target):
#             if(j>i):
#                 print(num[i],num[j])

'''9.integer into string format'''

# num = 91
# d1={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
# rev=""
# while(num>0):
#     rem = num%10
#     rev = d1[rem]+rev
#     num = num//10
# print(rev)
# print(type(rev))

'''10.string into integer format'''
# num = "91"
# d1={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
# rev = 0
# for i in num:
#     rev  = rev*10 + d1[i]
# print(rev)
# print(type(rev))

