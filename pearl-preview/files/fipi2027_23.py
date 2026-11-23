def f(c,e):
    p = str(c)
    if c>e: return 0
    if c==e: return 1
    if p[1]<p[2]: return f(c+1,e)+f(int(p[0]+p[2]+p[1]),e)
    return f(c+1,e)
print(f(100,141))
