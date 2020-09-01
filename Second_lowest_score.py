info=[]
names=[]
scores=[]
n=int(input())
if n>2 and n<=5:
    for i in range(n):
        na=input()
        ma=float(input())
        info.append([na,ma])
for j in range(len(info)):
    if info[j][1] not in scores:
        scores.append(info[j][1])
scores.sort()
lo=min(scores)
pos=0
for k in range(len(scores)):
    if lo==scores[k]:
        pos=k
print(pos)
se_lo=scores[pos+1]
for h in range(len(info)):
    if info[h][1]==se_lo:
        names.append(info[h][0])
names.sort()
for v in names:
    print(v)

