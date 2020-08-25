# python3
def compute_min_refills(distance, tank, stops):
    # write your code here
    stop = 0
    last_stop_value = 0
    index = 0
    stops.append(distance)
    while index < len(stops):
        if stops[index] - last_stop_value <= tank:
            index += 1
        elif stops[index] - stops[index - 1] > tank or index == 0:
            return -1
        else:
            last_stop_value = stops[index - 1]
            stop += 1
    return stop


# if __name__ == '__main__':
#     d, m, _, *stops = map(int, sys.stdin.read().split())
#     print(compute_min_refills(d, m, stops))


print(compute_min_refills(950, 400, [200, 375, 550, 750]))
