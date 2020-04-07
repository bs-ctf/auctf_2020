

num = [3, 7, 11, 37, 89, 237, 452]


message=""
with open("ciphertext.txt") as f:
    message=f.read()

message = message[1:-1]
message=list(map(int,message.strip().split(",")))