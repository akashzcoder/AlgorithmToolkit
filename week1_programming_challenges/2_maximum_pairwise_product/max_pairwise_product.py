# python3


#  2 pass
# def max_pairwise_product(numbers):
#     highest_index = -1
#     max_number = float('-inf')
#     len_numbers_arr = len(numbers)
#     second_max_number = float('-inf')
#     for i in range(len_numbers_arr):
#         if max_number < numbers[i]:
#             max_number = numbers[i]
#             highest_index = i
#     for i in range(len_numbers_arr):
#         if second_max_number < numbers[i] and i != highest_index:
#             second_max_number = numbers[i]
#     return max_number * second_max_number


# 1 pass
def max_pairwise_product(numbers):
    if len(numbers) < 2:
        return None
    max1, max2 = numbers[0], numbers[1]
    if numbers[1] > numbers[0]:
        max1, max2 = numbers[1], numbers[0]
    len_numbers_arr = len(numbers)
    for i in range(2, len_numbers_arr):
        if max1 < numbers[i]:
            max2 = max1
            max1 = numbers[i]
        elif max2 < numbers[i]:
            max2 = numbers[i]
    return max1 * max2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
