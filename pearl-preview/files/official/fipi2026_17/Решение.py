from pathlib import Path
f = Path(__file__).with_name("1_17.txt")
a = [int(x) for x in open(f)]
m = min(x for x in a if x>0 and x%123==0)
ans = []
for i in range(len(a)-1):
    if a[i]+a[i+1]<m: ans.append(a[i]+a[i+1])
print(len(ans),abs(max(ans)))
