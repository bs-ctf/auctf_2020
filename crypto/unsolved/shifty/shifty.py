#Unsolved


from collections import Counter 


ct=""
with open("ciphertext.txt") as f:
    ct=f.read()

count = Counter(ct)


print(count)

print(len(ct))