# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    if n < 0:
        return None
    var1 = 0
    var2 = 1
    new_var = 0
    for i in range(2, n+1):
        new_var = (var1 + var2) % 10
        var1, var2 = var2, new_var
    return new_var


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
