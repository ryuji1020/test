import numpy as np # nmpyの呼出？ <- yes
# フィボナッチ数列
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

# フィボナッチ数列2
def fib2(n):
    A=np.matrix([[0,1], [1,1]],dtype=np.int64)
    # Rはなくても良い
    R=np.matrix([[0], [1]],dtype=np.int64)
    # Aの[1, 1]要素がフィボナッチ数列
    R=A**(n-1)*R # Rによって行列の２列目のみを抽出
    return R[1,0] # 戻り値[1,0]はなに <- 行列中のフィボナッチ数列の要素抽出

# フィボナッチ数列3
def fib3(n):
    A=np.matrix([[0,1],[1,1]],dtype=np.int64)**(n-1)
    return A[1, 1]

if __name__ == '__main__':
    Fiblist = [fib(n) for n in range(1,100)]
    print(Fiblist) # [0,1,1,2,3,4,8,13,21]
