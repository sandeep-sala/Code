# Same as divide and conqure with sorting data
# Top-Down Memorization
# Bottom-Up Memorization Tabular (Avoid Recursion)

# Fibonacci Series With Memorization
# Top-Down Memorization
def fibMemo(n, memo={}):
    if n in [0,1]:
        return 0
    if n == 2:
        return 1
    if n not in memo:
        memo[n] = fibMemo(n-1, memo) + fibMemo(n-2, memo)
    return memo[n]

# Bottom-Up Memorization Tabular (Avoid Recursion)
def fibTab(n):
    tb = [0,1]
    for i in range(2,n+1):
        tb.append(tb[i-1]+tb[i-2])
    return tb[n-1]

print(fibTab(6))