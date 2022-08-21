from codecs import decode
string=bytearray(b"""To be fair, said the cat, I do not intend to steal you.
I would rather see you dead!
- Alright.""")
for n in range(len(string)):string[n]=(string[n]+n)%127
with open('text','wb') as f:f.write(string)
with open('text','rb') as f:string=bytearray(f.read())
for n in range(len(string)):string[n]=(string[n]-n)%127
print(decode(string))