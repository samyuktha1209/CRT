'''
Read a number from user and count the factors

n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

print("Number of factors:", count)

n = int(input())
if n >= 0:
    print(int(str(n)[::-1]))
else:
    n = -1*n
    print(-1*int(str(n)[::-1]))
'''
