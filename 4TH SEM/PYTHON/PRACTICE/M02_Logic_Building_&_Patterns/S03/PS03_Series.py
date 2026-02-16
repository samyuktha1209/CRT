'''
read a  and d values from the user and display upto 10 values from arithmetic progression
a=1 d=2
1,3,5,7
a,a+d,a+2*d,a+3*d
a+0*d
a+1*d
a+2*d



a+9*d


a=int(input())
d=int(input())
for i in range(10):
    print(a+ (i*d) ,end=" ")

how to print fibonacci series
recurise
list
memoization
n=5
[0,1,1,2,3] using list
a=0
b=1
n=int(input())
for i in range(n):
    a,b=b,a+b
    print(a,end=" ")
2.[0,1]
li[0]+li[1]
[0,1,1,-]
i=2
i-2 i-1
n=int(input())
li=[0,1]
for i in range(2,n):
    li.append(li[i-2]+li[i-1])
print(li)

3.power of a number
n=2
output:2,4,8,16

#input:2
#output:2,4,8,16
n=int(input())
for i in range(1,11):
    print(n**i,end=" ")
    
'''