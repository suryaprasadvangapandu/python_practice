'''
Task 1 : Create a program to: 
• Accept two integer values. 
• Perform addition, subtraction, multiplication, division, floor division, modulus, and exponentiation. 
• Display all results. '''
# n = int(input("Enter the value :"))
# m = int(input("Enter the value :"))
# print(f"Addition of two numbers : {n} + {m} = {n+m}")
# print(f"Addition of two numbers : {n} - {m} = {n-m}")
# print(f"Addition of two numbers : {n} / {m} = {n/m}")
# print(f"Addition of two numbers : {n} % {m} = {n%m}")
# print(f"Addition of two numbers : {n} **{m} = {n**m}")

'''
Task 2 : Create a program to: 
• Accept an integer.
 • Display: 
            - Value 
            - Data type
            - Memory address 
            - Object size 
'''
# n = int(input("Enter an Integer :"))
# print(f"Value of n : {n}")
# print(f"Data type of n : {type(n)}")
# print(f"Memory address of n : {id(n)}")
# print(f"Object size of n : {n.__sizeof__()}")

''' Task3 : Create a program to : 
• Accept collection of names as ['Ashish', 'Manish', 'Suresh', 'Vignesh', 'Jogesh'] 
• Accept Collection of Salaries as [67000, 25000, 80000, 35000, 15000]
• Findout the Highest Salary along with Person name 
• Findout the Lowest Salary along with Person name 
• Findout the median Salary belongs to which Person name '''
# names = ['Ashish','Manish','Suresh','vignesh','Jogesh']
# Salaries = [67000,25000,80000,35000,15000]
# hs = max(Salaries)
# ihs = Salaries.index(hs)
# h_person = names[ihs]
# print(f"The person with highest Salary is : {hs} -> {h_person}")

# ls = min(Salaries)
# ils = Salaries.index(ls)
# l_person = names[ils]
# print(f"The person with lowest Salary is : {ls} -> {l_person}")

# sort = sorted(Salaries)
# median = sort[len(sort)//2]
# i_median = Salaries.index(median)
# m_person = names[i_median]
# print(f"The person with median Salary is : {median} -> {m_person}")

'''Task 4 : Create a program to: 
• Convert integer into float. 
• Convert integer into string. 
• Convert integer into binary. 
• Convert integer into octal. 
• Convert integer into hexadecimal. 
• Convert integer into ASCII character.   
• Convert string into integer. 
• Convert string(Word) into List. 
• Convert string(Word) into Set. 
• Convert string(sentence) into List of words. 
• Convert string(Character) into ASCII Value.   
NOTE : Display the data type after each conversion using type(). '''
# n = 65
# print("Value of n :",n)
# f1= float(n)
# print(f"convert integer into float is {f1} and datatype is {type(f1)}" )
# s1 = str(n)
# print(f"convert integer into string is {s1} and datatype is {type(s1)}" )
# b1 = bin(n)
# print(f"convert integer into binary is {b1} and datatype is {type(b1)}" )
# oct1 = oct(n)
# print(f"convert integer into octal is {oct1} and datatype is {type(oct1)}" )
# hex1 = hex(n)
# print(f"convert integer into hexadecimal is {hex1} and datatype is {type(hex1)}" )
# asc1 = chr(n)
# print(f"convert integer into ascii is {asc1} and datatype is {type(asc1)}" )

# str1 = "10"
# integer = int(str1)
# print(f"convert string into integer is {integer} and datatype is {type(integer)}" )

# str2 = "surya"
# l1 = list(str2)
# print(f"convert  string(Word) into List is {l1} and datatype is {type(l1)}" )
# s1 = set(str2)
# print(f"convert  string(Word) into Set is  {s1} and datatype is {type(s1)}" )

# str3 ="my name is surya"
# sp1 = str3.split()
# print(f"convert  string(sentence) into List of words is {sp1} and datatype is {type(sp1)}" )

# str4 = 'A'
# asc2 = ord(str4)
# print(f"convert string(Character) into ASCII Value is {asc2} and datatype is {type(asc2)}" )


'''
Task 5 : Create a program to: 
• Accept student name, age, CGPA, and department.
• Display all information using: 
                o format() 
                o f-string 
                o % formatting 
• Display the data type of each value. 
 '''
# name = input("Enter the name :")
# age = int(input("Enter the Age :"))
# cgpa = float(input("Enter the cgpa :"))
# department = input("Enter the department :")

# print("%s is an Student in Sasi College and his age is %d years and he got the %.1f cgpa and he belongs to %s department"%(name,age,cgpa,department))
# print("Datatype of name is %s and age is %s and cgpa is %s and department is %s"%(type(name),type(age),type(cgpa),type(department)))
# print()
# print("{} is an Student in Sasi College and his age is {} years and he got the {} cgpa and he belongs to {} department".format(name,age,cgpa,department))
# print("Datatype of name is {} and age is {} and cgpa is {} and department is {}".format(type(name),type(age),type(cgpa),type(department)))
# print()
# print(f"{name} is an Student in Sasi College and his age is {age} years and he got the {cgpa} cgpa and he belongs to {department} department")
# print(f"Datatype of name is {type(name)} and age is {type(age)} and cgpa is {type(cgpa)} and department is {type(department)}")



'''Task 6 : Create a program to: 
• Pack multiple values into a list.
• Unpack them into separate variables. 
• Display every variable.
• Multiple assignment 
• Swapping two variables without a temporary variable. '''
# l1 = ["surya",20,9.2,"cse"]
# print("Packed Data :",l1)
# print()
# name = l1[0]
# age = l1[1]
# cgpa = l1[2]
# department= l1[3]

# print("name is :",name)
# print("age is :",age)
# print("cgpa is :",cgpa)
# print("department is :",department)
# print()
# a,b,c = 30,40,50
# print("a value is ",a)
# print("b value is ",b)
# print("c value is ",c)


# x = 10
# y = 20
# print(" before swapping is, x =", x)
# print(" before swapping is ,y =", y)

# x = x + y #x=30
# y = x - y #y= 10
# x = x - y #x=20
# print()
# print(" after swapping is , x =", x)
# print("after swapping is , y =", y)


'''Task 7 : Create a program demonstrating: 
• Concatenation 
• Repetition 
• Membership 
• Identity 
• Equality using both lists and tuples.'''
# l1 = [10, 20, 30]
# l2 = [40, 50, 60]
# print("===list operations====")
# print("concatination :",l1+l2)
# print("Repetition :",l1*2)
# print("Membership :",40 not in l1)
# print("Identity :",l2 is not l1)
# print("Equality :",l1==l1)

# t1=(10,20,30)
# t2 = (40,50,60)
# print("===tuple operations===")
# print("concatination :",t1+t2)
# print("Repetition :",t1*2)
# print("Membership :",40 not in t1)
# print("Identity :",t2 is not t1)
# print("Equality :",t1==t1)

'''Task 8 : Create a program to
• convert the string s1="IT" into "IT@IT@IT@IT@IT" using single line expression. 
• convert the string "HeLlO " into "hELLO$hEllo$hELLO" using string built-in functions. 
NOTE : $ symbol should not be concatenate by using + Operator. 
'''
# s1= "IT"
# exp1 = (s1+"@")*4+s1
# print("Final Expression is :",exp1)

# s2 = "HeLlo"
# exp = s2.title().swapcase()+" "+s2[0].lower() + s2[1].upper() + s2[2:].lower()+" "+s2.title().swapcase()
# exp2 = exp.replace(" ","$")
# print(exp2)

'''Task 9 : Create a program to 
• create a string that contains another string in the middle position of it's string.
 (Ex: input1="Helo",input2="Hi" output: 'HeHilo') 
 NOTE : Numbers won’t be show in slice operator if I see your code. So don’t take directly numbers in slice operator even if you need.  
• convert the string "Python" into "nhyPto" by using slice operator and don’t use indexing. 
NOTE : Numbers won’t be show in slice operator if I see your code. So don’t take directly numbers in slice operator even if you need'''
# s1 = "Helo"
# s2 = "Hi"

# mid = len(s1) // 2
# print(s1[:mid] + s2 + s1[mid:])

# s2 = "Python"
# print(s2[len(s2)-1::-2]+s2[:len(s2)-1:2])


'''Task 10 : Create a program to prove that following both strings are anagram. 
S1 = "Silent" S2 = "Listen" 
NOTE : Here, s1 and s2 strings are containing same alphabets but in different positions. 
According Anagram Concept, You can change the alphabets cases both as same and you can prove.'''

# s1 = "Silent"
# s2 = "Listen"

# l1 = []
# l2 = []

# for i in s1:
#     l1.append(i.lower())

# for j in s2:
#     l2.append(j.lower())

# l1.sort()
# l2.sort()

# if l1 == l2:
#     print("Anagram")
# else:
#     print("Not a Anagram")


'or'

# word1 = input("Enter the word1 : ")
# word2 = input("Enter the word2 : ")
# sort1 = sorted(word1.lower())
# sort2 = sorted(word2.lower())
# if(sort1==sort2):
#     print("Both strings are Anagram")
# else:
#     print("not an Anagram")



'''
Task 11 : Create a program to • Update the value in position of the strings as 
which are starting with 'M' as True otherwise False to the list 
['Rudra', 'Mahesh', 'Nandini', 'Mohit'] as follows : #Output : [False, True, False, True] 

'''

# names = ['Rudra', 'Mahesh', 'Nandini', 'Mohit']

# result = []

# for name in names:
#     result.append(name.startswith("M"))

# print(result)




'''Task 12 : Create a program to • Modify the list ['2', True, False, 'Four'] as below mentioned reqn 
#Output : ['22', '1', '0', '4444'] '''

# l1 = ['2', True, False, 'Four']

# l2 = []

# for i in l1:
#     if i == '2':
#         l2.append('22')
#     elif i == True:
#         l2.append('1')
#     elif i == False:
#         l2.append('0')
#     elif i == 'Four':
#         l2.append('4444')

# print(l2)

'''
Task 13 : • Create a Program to store all resume details using appropriate data types 
and display them using multiple string formatting techniques.'''

# name = "Surya Prasad"
# age = 22
# phone = 9030790186
# email = "surya@gmail.com"
# cgpa = 9.4
# gender = "Male"
# qualification = "B.Tech"
# department = "Computer Science"
# skills = ["Python", "HTML", "CSS", "JavaScript"]
# experience = 1
# is_fresher = True
# address = "Hyderabad"

# print("Name       : %s" % name)
# print("Age        : %d" % age)
# print("Phone      : %d" % phone)
# print("Email      : %s" % email)
# print("CGPA       : %.1f" % cgpa)

# print()

# print("Name       : {}".format(name))
# print("Qualification : {}".format(qualification))
# print("Department : {}".format(department))
# print("Experience : {} years".format(experience))

# print()

# print(f"Name       : {name}")
# print(f"Gender     : {gender}")
# print(f"Skills     : {skills}")
# print(f"Address    : {address}")
# print(f"Fresher    : {is_fresher}")







