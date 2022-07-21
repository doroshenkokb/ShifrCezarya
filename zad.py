import re

txt = input()
txt2 = [len(i) for i in re.findall(r'\b\w+\b',txt)]
# print(txt2)

c = 'abcdefghijklmnopqrstuvwxyz'
C = c.upper()
ss=''
count=0


for i in txt.split():
    # print(i)
    for k in i:
        if k in c:
          k = c[c.find(k)+txt2[count]]
          ss+=k
        elif k in C:
          k = C[C.find(k) + txt2[count]]
          ss += k
        elif k == k:
          k = k
          ss += k
    ss+=" "
    count+=1
print(ss)











