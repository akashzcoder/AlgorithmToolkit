# Uses python3
import sys


def lcm_naive(a, b):
    larger = max(a, b)
    smaller = min(a, b)
    lcm = larger
    while lcm % smaller != 0:
        lcm += larger
    return lcm


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
