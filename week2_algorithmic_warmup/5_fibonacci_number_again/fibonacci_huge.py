# Uses python3
import sys


def get_mod_value(m_copy):
    count = 1
    while m_copy > 0:
        count *= 10
        m_copy = int(m_copy/10)
    return count


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    previous = 0
    current = 1
    mod_value = get_mod_value(m)
    val = n % 60
    for _ in range(2, val):
        previous, current = current, (previous + current) % mod_value
    return current % m


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
