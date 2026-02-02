'''for and while
Syntax:
for variable in iterable:
       #code block to be executed
n = int(input("Enter a num: "))
for i in range(1,n+1):
   print(i)

n = int(input("Enter a num:"))
for i in range(1,n+1):
    print(i,end=" ")
i = 1
while i <= n:
    print(i)
    i += 1

name = "Chelli Samyuktha"
i = 0
while i <=5:
    print(name)
    i += 1
print(len(name))

name = "Chelli Samyuktha"
i = len(name) - 1
while i >= 0:
    print(i,name[i])
    i -= 1

s = "Chelli Samyuktha"
rev = "".join(reversed(s))
print(rev) 
'''
n = int(input())
marks = list(map(int, input().split()))

marks = marks[:n]   # take only first n marks

count = 0
for m in marks:
    if m >= 35:
        count += 1

pass_percent = (count / n) * 100
fail_percent = ((n - count) / n) * 100

print(pass_percent)
print(fail_percent)
print(count)
 