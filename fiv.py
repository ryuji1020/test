import numpy as np                  #nmpyの呼出？
def fib(n, memo={}):
        if n == 1:
            return 0
        elif n==2:
            return 1
        elif n in memo:
            return memo[n]
        else:
            memo[n] = fib(n-1, memo) + fib(n-2, memo)
            return memo[n]

#    A=np.matrix([[0,1],             #フィボナッチ数列
#        [1,1]],dtype=np.int64)
#    R=np.matrix([[0],
#        [1]],dtype=np.int64)
#    R=A**(n-1)*R

#    return R[1,0]#戻り値 [1,0]はなに

Fiblist=[]
for n in range(1,100):
    Fiblist+=[fib(n)]

print(Fiblist)
    # [0,1,1,2,3,4,8,13,21]
