# -*- coding: cp1252 -*-
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

msg = raw_input("Enter the msg ")
key = raw_input("Enter the key ")
key = int(key)
msg = msg.lower()
encrypt=""
for i in msg:
        if i != ' ':
            v = alpha.index(i)
            d = v + key
            a  = d%26
            encrypt = encrypt + alpha[a]
        else:
            encrypt = encrypt + i

print "Encrypted Message :" + encrypt

decrypt=""
for i in encrypt:
        if i != ' ':
            v = alpha.index(i)
            d = v - key
            a  = d%26
            decrypt = decrypt + alpha[a]
        else:
            decrypt = decrypt + i

print "Decrypted Message :" + decrypt
