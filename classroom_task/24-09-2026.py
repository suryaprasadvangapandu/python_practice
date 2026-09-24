'''1.numbers divisible by the 5 in list'''

# l1 = [i for i in range(1,101) if(i%5==0)]
# print(l1)

'''2.prime numbers'''
# num = 100
# l1 = [i for i in range(1,num+1) if(i%2==0)]
# print(l1)

'''3.palindrome number'''
# num = 1000
# l1 = [i for i in range(1,1000) if (str(i) == str(i)[::-1])]
# print(l1)

'''4.perfect number'''
# num =1000
# l1 =[i for i in range(1,num+1)  if(sum(j for j in range(1,i) if(i%j ==0))==i)]
# print(l1)

'''5.factor in that prime numbers in the list'''

# num = 100
# l1 = [{i:[j for j in range(2,i+1) if(i%j == 0 and sum(1 for k in range(1,j+1) if j%k==0) ==2)]} for i in range(1,num+1)]
# print(l1)

