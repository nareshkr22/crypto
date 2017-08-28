import random


cipher = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
plain = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
random.shuffle(cipher)
print cipher

print plain
msg = raw_input("Enter the msg ")
msg = msg.lower()
encrypt=""
for i in msg:
        if i != ' ':
            v = plain.index(i)          
            encrypt = encrypt + cipher[v]
        else:
            encrypt = encrypt + i

decrypt=""
for i in encrypt:
        if i != ' ':
            v = cipher.index(i)          
            decrypt = decrypt + plain[v]
        else:
            decrypt = decrypt + i


print encrypt

print decrypt
