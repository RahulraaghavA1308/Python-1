def fibo(n):
    f = -1
    s = 1
    for i in range(n + 1):
        t = f + s
        f = s
        s = t
    return t

def max(num):
    max = num[0]
    for i in num:
        if max < i:
            max = i
    return max