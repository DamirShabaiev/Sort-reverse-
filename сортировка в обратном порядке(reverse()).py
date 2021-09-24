n = ['a','b','c','d']
N = len(n) // 2
s = 0
for i in range(N):
    n[i],n[i-1-s] = n[i-1-s],n[i]
    s += 2
    print(n)
    
