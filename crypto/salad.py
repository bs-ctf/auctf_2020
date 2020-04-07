#Caesar encryption

# I'll Have The Salad

ct = "vpxoa{eP5o_4_R4mH_pK_1_4421_9952}"

key = ord(ct[0]) - ord('a')

pt=""

for i in ct:
    if i.isupper():
        tmp = chr(((ord(i) - key-ord('A'))%26)+ord('A'))
        pt+=tmp
    elif i.islower():
        tmp = chr(((ord(i) - key-ord('a'))%26)+ord('a'))
        pt+=tmp
    #elif i.isnumeric():
    #    tmp = chr(((ord(i) - key-ord('0'))%10)+ord('0'))
    #    pt+=tmp
    else:
        pt+=i

print(pt)