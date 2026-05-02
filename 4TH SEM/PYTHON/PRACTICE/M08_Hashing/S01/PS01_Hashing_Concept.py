'''
Hashing:
Defination:
Advantages:
Hashing Mechanism:
Hash key value:
hash function:
collision resolution techniques:
1.separate chaining
2.open addressing
   --> Linear probing
   --> Quadratic probing
   --> Double hashing

a = 10
b = 'sam'
c = 12.12
print(hash(a))
print(hash(b))
print(hash(c))
'''

size = 7
table = [None]*size
a = [10,20,30]
for key in a:
    index= key % size
    table[index]= key
print(table)