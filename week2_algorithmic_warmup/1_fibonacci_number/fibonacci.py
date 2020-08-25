# Uses python3
def calc_fib(n):
    if n < 0:
        return None
    if n <= 1:
        return n
    var1 = 0
    var2 = 1
    new_var = 0
    for i in range(2, n+1):
        new_var = var1 + var2
        var1, var2 = var2, new_var
    return new_var


n = int(input())
print(calc_fib(n))
