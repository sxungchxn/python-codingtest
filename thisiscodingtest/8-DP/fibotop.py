# top-down
dp = [0] * 100

# 위쪽에서 부터 값을 찾기 위해 아래로 향하는 방식


def fibo(n):
    if n == 1 or n == 2:
        return 1
    if dp[n] != 0:
        return dp[n]
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]
