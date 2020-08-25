# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    # write your code here
    if capacity == 0:
        return 0
    value = 0
    v_w = [(v/w, v, w) for v, w in zip(values, weights)]
    v_w.sort(key=lambda v_w: v_w[0], reverse=True)
    count = 0
    while capacity > 0:
        if capacity > v_w[count][2]:
            capacity -= v_w[count][2]
            value += v_w[count][1]
        else:
            value += capacity * v_w[count][0]
            capacity = 0
        count += 1
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
#     weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
