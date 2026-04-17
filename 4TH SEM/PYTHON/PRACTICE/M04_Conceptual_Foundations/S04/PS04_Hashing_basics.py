#Frequency count
def frequency_count(st):
    d = {}
    for char in st:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return d

print(frequency_count("abcabc"))#{'a':2,'b':2,'c':2}