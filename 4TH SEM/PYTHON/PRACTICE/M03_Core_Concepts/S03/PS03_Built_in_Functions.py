'''ng 
1.Find Largest Number(Using max())
a=[1,2,5,9,63]
print(max(a))
2.Check palindrome(using reverse() & join)
s=input("enter a string")
if s=="".join(reversed(s)):
    print("Palindrome")
else:
    print("Not Palindrome")
3.Count even numbers(Using filter())

a=[1,2,5,8,9,63]
res=list(filter(lambda x:x%2==0,a))
print(res)
print(len(res))
4) Remove Duplicates(Using set())
5)sum of digits(using sum())
n=12345
res=sum(int(digit) for digit in str(n))
print(res)
6) sort words alphabetically(using sorted())
'''
a=['Kal','Thanu','Anu']
print(list(sorted(a)))