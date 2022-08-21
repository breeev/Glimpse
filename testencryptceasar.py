from codecs import decode


string=bytearray(b"""To be fair, said the cat, I do not intend to steal you.
I would rather see you dead!
- Alright.""")
for n in range(len(string)):string[n]=(string[n]+n)%128
# print(decode(string))
for n in range(len(string)):string[n]=(string[n]-n)%128
print(decode(string))