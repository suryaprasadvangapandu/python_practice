#WAP to check whether a number is Amstrong Number or not
n= 153
temp = n
sum = 0 #-->27+125+1-->153
while(n>0):
    rem = n%10 #153-->3-->5-->1
    sum = sum+rem**len(str(temp)) #"153"-->>3-->27-->5**3-->125-->1**3
    n = n//10 #153//10 #-->15 -->1
if(temp == sum):
    print("Armstrong")
else:
    print("Not Armstrong")