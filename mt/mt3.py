'''task-1'''
# sal= [25000, 30000, 45000, 28000, 35000]
# print("Orginal salary list is ",sal)
# sal.append(40000)
# sal.append(50000)
# print("updated salary is ",sal)
# sal.remove(28000)
# print("removed salary is :",sal)
# sal.sort()
# print("Sorted salary is :",sal)
# sal.sort(reverse=True)
# print("Reversed Salary is :",sal)
# print("Highest Salary is ",sal[0])
# print("Lowest Salary is ",sal[-1])

'''task-2'''
# emp_id =(101, 102, 103, 104, 105,106,102)
# print("First employee is ",emp_id[0])
# print("middle employee is ",emp_id[len(emp_id)//2])
# print("Last employee is ",emp_id[-1])

# middle_index= len(emp_id)//2 
# print("Middle index is :",middle_index)

# print("first half is :",emp_id[:middle_index])
# print("second half is :",emp_id[middle_index:])

# new_ids = (107,108)
# updated_emp_id = emp_id+new_ids
# print("updated employee ids after adding new ids is ",updated_emp_id)
# print("repeat employee id's twice : ",emp_id*2)
# print("count of Employee Id 102:",emp_id.count(102))
# print("Index od Employee Id 105 :",emp_id.index(105))

'''task-3'''
# teamA = {"Bharath", "Surya", "Saikiran", "aravind", "Suresh"}
# teamB = {"Surya", "Saikiran", "Sai", "karthik", "Suresh"}

# print("Common players from teamA and TeamB is ",teamA.intersection(teamB))
# print("Unique elements from teamA is",teamA.difference(teamB))
# print("Unique elements from teamB is",teamB.difference(teamA))
# print("Total Players is ",teamA.union(teamB))
# print("subset is",teamA.issubset(teamB))
# print("superset is",teamB.issuperset(teamA))
# print("remove the team-A players :",teamA.clear())

'''task-4'''

# students = [
#     {
#         "name": "Surya",
#         "branch": "CSE",
#         "year": 4,
#         "marks": (85, 90, 88)
#     },
#     {
#         "name": "Ravi",
#         "branch": "ECE",
#         "year": 3,
#         "marks": (80, 75, 82)
#     },
#     {
#         "name": "Kiran",
#         "branch": "EEE",
#         "year": 2,
#         "marks": (70, 78, 75)
#     }
# ]

# print("Student details is :",students)

# print("first student details is ",students[0])

# students[1]["name"] = "karthik"
# print("updated name in the second student details :",students[1])

# students.append({"name":"vihan","branch":"CSE","year":2,"marks":(80,40,50)})
# print("Adding in a student in the list :",students)

# print("Remove one student is :",students.pop(2))

# for student in students:
#     for key, value in student.items():
#         if key == "marks":
#             print(key ,value)

# student1 = students.copy()
# print(student1)

'''task-5'''

# student = {
#     "Roll No": 101,
#     "Name": "Surya",
#     "Branch": "CSE",
#     "Year": 4,
#     "CGPA": 8.5
# }
# print("Student details :")
# for key, value in student.items():
#     print(key, ":", value)

# student["CGPA"] = 9.0
# print("After updating CGPA:", student)
# student.update([("email","surya@gmail.com"),("Year",5)])
# print("After adding the email and updating the year value is ",student)
# student.pop("Year")
# print("Removing the year is :",student)
# student_copy = student.copy()
# print("copied dictionary is ", student_copy)
# student_copy.clear()
# print("copied dictionary after clear is ", student_copy )

'''task-6'''
# mobile = {
#     "Brand": "Samsung",
#     "Model": "Galaxy S24",
#     "RAM": "8GB",
#     "Color": "Black"
# }

# print("Before Modification:")
# for key, value in mobile.items():
#     print(key, ":", value)
# mobile.update([("Battery Capacity","4000mAh")])
# print("after adding the battery capacity is ",mobile)
# mobile["RAM"] = "12GB"
# print("After updating the mobile ram is :",mobile)
# mobile.pop("Color")
# print("After removing the color is :",mobile)

# print("Total number of items:", len(mobile))

# mobile_copy = mobile.copy()

# print("Copied Dictionary:", mobile_copy)

# print("After Modification:")
# for key, value in mobile.items():
#     print(key, ":", value)

'''task-7'''

# s1 = "surya123"
# dec= sorted(s1,reverse=True)
# print("decending order of string",dec)
# if s1[0].isalpha() and s1[0].lower() not in "aeiou":
#     print("yes")
# else:
#     print("No")
# if s1[-1].isdigit():
#     print("Yes")
# else:
#     print("No")
# if s1[0].isupper():
#     print("Yes")
# else:
#     print("No")

'''task-8'''

# num = int(input("Enter the integer number :"))

# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")

'''task-9'''

'''n = 5
for i in range(1,n+1):
    print("  "*(n-i)+"* "*(2*i-1))

        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * '''

'''n = 5
for i in range(1,n+1):
    print(" "*(i-1)+"* "*n)

* * * * * 
 * * * * * 
  * * * * * 
   * * * * * 
    * * * * * '''

'''n= 5
for i in range(1,n+1,):
    print(" "*(n-i)+"* "*n)

    * * * * * 
   * * * * * 
  * * * * * 
 * * * * * 
* * * * * '''

'''n=5
for i in range(1,n+2):
    print("  "*(n+1-i),(i-1)*" *"+"|"+"* "*(i-1))
           |
          *|* 
        * *|* * 
      * * *|* * * 
    * * * *|* * * * 
  * * * * *|* * * * * '''

"--Task-10--"

'''num = 5
for i in range(1,num+1):
    for j in range(i):
        print(i,end=" ")
    print()
for i in range(1,num+1):
    for j in range(num-i):
        print(num-i,end=" ")
    print()

1
22
333
4444
55555
4444
333
22
1'''



'''num = 5

for i in range(num, 0, -1):

    print("|", end="")

    for j in range(num - i):
        print("  ", end="")

    print(i, end="")

    for j in range((i - 1) * 2):
        print("  ", end="")

    if i != 1:
        print(i, end="")
    for j in range(num - i):
        print("  ", end="")
    print("|", end="")
    print()

|5                5|
|  4            4  |
|    3        3    |
|      2    2      |
|        1        |

'''



'''num = 5

for i in range(1, num + 1):
    for j in range(i):
        print(chr(65 + i - 1), end="")
    print()

A
BB
CCC
DDDD
EEEEE'''



'''num = 5
for i in range(1,num+1):
    for j in range(num-i+1):
        print(" ",end="")
    for j in range(i):
        print(chr(65 + i - 1), end=" ")
    print()

     A 
    B B 
   C C C 
  D D D D 
 E E E E E '''



'''
num = 5
for i in range(num,0,-1):
    for j in range(num-i+1):
        print(" ",end="")
    for j in range(i):
        print(chr(65 + i - 1), end=" ")
    print()

 E E E E E 
  D D D D 
   C C C 
    B B 
     A '''