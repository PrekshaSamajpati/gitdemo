n=int(input("enter the number of strings: "))
list=[]
for i in range(n):
    str=input(f"enter string:{i+1}")
    list.append(str)
counts={}
for word in list:
    word=word.lower()
    for char in word:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
print(counts)
