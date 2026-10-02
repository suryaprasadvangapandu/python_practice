def isAnagram(s1,s2):
        if len(s1) != len(s2):
            print("Not Anagram")
        else:
            count = 0

            for i in s1:
                for j in s2:
                    if i == j:
                        count = count + 1
                        break
        return count == len(s1)
s1 =input("Enter the 1st string : ")
s2 = input("Enter the 2nd String : ")
print(isAnagram(s1,s2))