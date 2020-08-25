# Uses python3
import sys


# [1, 5, 10]
def get_change(m):
    """

    :param m:
    :return:
    """
    results = 0
    coins = [10, 5, 1]
    while m > 0:
        for i in coins:
            num = m//i
            results += num
            m %= i
    return results


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
