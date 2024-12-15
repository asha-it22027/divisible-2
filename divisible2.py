import math
n=int(input("Enter the size of the first array: "))
if n<=20 or n%10!=0:
    print("Invalid input")
    exit()
print("Enter the elements of first array: ")
arr1=list(map(int,input().split()))
m=n//10
print("Enter the elements of second array: ")
arr2=list(map(int,input().split()))
result=[]
for i in range(m):
    a=arr1[i*10]
    b=arr2[i]
    if b==0:
        print("Division by zero detected.")
        exit()
    divisor=math.ceil(a/b)
    rem=a%b
    result.append((divisor,rem))
    print(f"Results(Divisor, Rem): {divisor}, {rem}")