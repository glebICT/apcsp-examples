def smallest(numbers):
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            return number
    return min_value

smallest([5, 3, 8, 1, 4])

#Alternative better version
# def smallest(numbers):
#     min_value = numbers[0]
#     for number in numbers:
#         if number < min_value:
#             min_value = number
#     return min_value