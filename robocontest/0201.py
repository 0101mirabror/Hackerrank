def find_number_combinations(numbers, target):
    result = []
    backtrack(numbers, target, [], result)
    return result

def backtrack(numbers, target, combination, result):
    if target == 0:
        result.append(combination)
        return
    if target < 0:
        return
    for i in range(len(numbers)):
        num = numbers[i]
        backtrack(numbers[i:], target - num, combination + [num], result)

print(len(find_number_combinations([1, 2], int(input()))))







# def find_number_combinations(numbers, target):
#     result = []
#     backtrack(numbers, target, [], result)
#     return result

# def backtrack(numbers, target, combination, result):
#     if target == 0:
#         result.append(combination)
#         return
#     if target < 0:
#         return
#     for i in range(len(numbers)):
#         num = numbers[i]
#         backtrack(numbers[i:], target - num, combination + [num], result)

# # Test case
# number_list = [1, 2]
# target_number = 526

# combinations = find_number_combinations(number_list, target_number)

# # Print the combinations
# print(len(combinations))
# # for combination in combinations:
# #     print(combination)