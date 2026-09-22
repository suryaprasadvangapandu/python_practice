'''--task-1--
WAP to check whether two strings are Anagram or not
   Ex:
   word1 = "Listen"
   word2 = "Silent"
   OP : Both strings are Anagram'''

# word1 = input("Enter the word1 : ")
# word2 = input("Enter the word2 : ")
# sort1 = sorted(word1.lower())
# sort2 = sorted(word2.lower())
# if(sort1==sort2):
#     print("Both strings are Anagram")
# else:
#     print("not an Anagram")

'''or'''
# word1 = input("Enter the word1 : ")
# word2 = input("Enter the word2 : ")

# word1 = word1.lower()
# word2 = word2.lower()

# if len(word1) != len(word2):
#     print("Not an Anagram")
# else:
#     count = 0

#     for i in word1:
#         for j in word2:
#             if i == j:
#                 count = count + 1
#                 break

#     if count == len(word1):
#         print("Both strings are Anagram")
#     else:
#         print("Not an Anagram")

'''
--task-2--
WAP to check whether a string a palindrome or not (W/O using any built-in function or slicing)'''

# word = input("Enter the word : ")
# rev = ""
# for w in word:
#     rev=w+rev

# if(rev==word):
#     print(f"{word} is a palindrome")
# else:
#     print(f"{word} is not a palindrome")

'''--task-3--
 WAP to findout the frequency of each character in the string.
   Ex: (W/O using any built-in functions)
   role = "Engineer"
   #OP : 
   {'E':1, 'n':2, 'g':1, 'i':1, 'e':2, 'r':1}'''
# word = input("Enter the word : ")

# freq = {}

# for ch in word:
#     if ch in freq:
#         freq[ch] = freq[ch] + 1
#     else:
#         freq[ch] = 1

# print(freq)


'''--task-4--
 WAP to findout the longest word from the sentence
   Ex:
   sentence = "Rajesh is a Senior Angular Developer in Cognizant Company"
   #OP:
   Developer
   Cognizant'''
# sentence = input("Enter the sentence : ")
# words = sentence.split()
# long = 0
# for word in words:
#     if(len(word)>long):
#         long = len(word)
# for word in words:
#     if(len(word)== long):
#         print(word)

'''--task-5--
WAP to findout the lowest value from the existing list
   (W/O using min() or sort() or sorted())
   Ex:
   nums = [2, 8, -1, 4, 7]
   #OP : -1'''

# endval= int(input("Enter the end value : "))
# nums =[]
# for i in range(endval):
#     num = int(input("Enter the numbers : "))
#     nums.append(num)
# low = nums[0]
# high = nums[0]
# for num in nums:
#     if(num <low):
#         low = num
# for num in nums:
#     if(num>high):
#         high = num
# print(low)
# print(high)



'''---task-6---
WAP to convert the first and last character of each word into uppercase and rest characters should be in lowercase
   Ex:
   sentence = "Rajesh is a Senior Angular Developer in Cognizant Company"
   #OP :
   "RajesH IS A SenioR AngulaR DevelopeR IN CognizanT CompanY"'''

# sentence = input("Enter the sentence : ")
# words = sentence.split()
# result = ""
# for word in words:
#     if(len(word)==1):
#         word = word.upper()
#     elif(len(word)>1):
#       word = word.lower()
#       word = word[0].upper()+word[1:-1]+word[-1].upper()
#     result=result+word+" "
# print(result)

'''--task-7--
WAP to generate the Prime Numbers in between a range from dynamic input. prime numbers have to store in list format only.
   Ex:
   begin = -10
   end = 20
   #OP :
   [2, 3, 5, 7, 11, 13, 17, 19]'''

# begin = int(input("Enter the begin value : "))
# end = int(input("Enter the end value : "))
# prime = []
# for num in range(begin,end):
#       if(num>1):
#         count = 0
#         for i in range(1,num+1):
#             if(num%i==0):
#                 count += 1
#         if(count==2):
#             prime.append(num)
# print(prime)

'''--task-8--
 WAP to swap the cases of each alphabet in the existing string without using any built-in function. (Don't use ord() or chr())
   Ex:
   city = "Chennai"
   #OP:
   'cHENNAI' '''

# city = input("Enter the String : ")

# lower = "abcdefghijklmnopqrstuvwxyz"
# upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# result = ""

# for ch in city:
#     for l, u in zip(lower, upper):
#         if ch == l:
#             result = result + u
#             break
#         elif ch == u:
#             result = result + l
#             break
#     else:
#         result = result + ch

# print(result)

'''--task-9--
WAP to check whether the string is containing only alphabets or not. 
   (without using any built-in function)
   Ex:
   word = "Birla Mandir"  #OP : False
   word = "Museum" #OP : True'''

# word = input("Enter the word : ")
# count = 0
# l1 = []
# l2 = []
# for i in word:
#    if(i in "1234567890" or i in " @#$%^&*().,"):
#       count =  0
#       break
#    else:
#       count = 1



# if(count == 1):
#    print("True")
# else:
#    print("False")


'''--task-10--
WAP to generate the mathematical multiplication tables of each number in between the range. Each table has to be in horizontal format only but take numbers from end to begin and each table also should be in reverse format.

    begin = 5
    end = 8'''

# begin = int(input("Enter the begin range : "))
# end = int(input("Enter the end range : "))

# for i in range(1,11):
#    for j in range(begin,end+1):
#       print(f"{j} X {i} = {i*j}",end="\t")
#    print()

