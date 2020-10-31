# *************** HOMEWORK 2 ***************
# GOOD LUCK!

# ************************ QUESTION 1 **************************
def print_triangle(size, start, end, direction):
    # this function print triangle in vertical direction with given the size of the rows and the direction
    asterisk = "*"
    back_space = ' '
    # prints over loop from start to end variable and prints backspace with asterisks
    for i in range(start, end, direction):
        print(back_space * (size - i) + asterisk * (2 * i - 1) + back_space * (size - i))


def rhombus(side_size):
    # this function print rhombus vertically using help function that prints 2 triangle in opposite direction
    print_triangle(side_size, 1, side_size, 1)
    print_triangle(side_size, side_size, 0, -1)


# ************************ QUESTION 2 **************************
def sort_list_min_to_max(list_numbers):
    for i in range(1, len(list_numbers)):
        for j in range(0, len(list_numbers) - i):
            if list_numbers[j] > list_numbers[j + 1]:
                list_numbers[j], list_numbers[j + 1] = list_numbers[j + 1], list_numbers[j]
    return list_numbers


def remove_dup_lists(list_numbers):
    no_dup_list = []
    for nes_list in list_numbers:
        if nes_list not in no_dup_list:
            no_dup_list.append(nes_list)
    return no_dup_list


def sort_sum_nested_list(list_numbers):
    for i in range(1, len(list_numbers)):
        for j in range(0, len(list_numbers) - i):
            if sum(list_numbers[j]) > sum(list_numbers[j + 1]):
                list_numbers[j], list_numbers[j + 1] = list_numbers[j + 1], list_numbers[j]
    return list_numbers


def lagrange_four_square_theorem(num):
    lagrange_list = []
    for i in range(int(num ** 0.5) + 1):
        for j in range(int(num ** 0.5) + 1):
            for k in range(int(num ** 0.5) + 1):
                for m in range(int(num ** 0.5) + 1):
                    if ((i ** 2) + (j ** 2) + (k ** 2) + (m ** 2)) == num:
                        temp_l = sort_list_min_to_max([i, j, k, m])
                        if temp_l not in lagrange_list:
                            lagrange_list.append(temp_l)
        # for small_list in lagrange_list:
        #   sort_list(small_list)
        # lagrange_list = remove_dup_lists(lagrange_list)
    lagrange_list = sort_sum_nested_list(lagrange_list)
    return lagrange_list


# ************************ QUESTION 3 **************************
def sort_list_max_to_min(list_numbers):
    for i in range(1, len(list_numbers)):
        for j in range(0, len(list_numbers) - i):
            if list_numbers[j] < list_numbers[j + 1]:
                list_numbers[j], list_numbers[j + 1] = list_numbers[j + 1], list_numbers[j]
    return list_numbers


def max_number_divide_3(numbers):
    # This function get list of numbers and return the maximum number in the list that divide in 3
    max_num = -1
    numbers = sort_list_max_to_min(numbers)
    for num in numbers:
        if num % 3 == 0 and num != 0:
            max_num = num
            break
    return max_num


def odd_range(numbers):
    # This function get list of numbers and return the length of longest series of odd numbers in the list
    series_counter = long_series = 0
    if numbers[0] % 2 != 0:
        long_series += 1
        series_counter += 1
    for i in range(1, len(numbers)):
        if numbers[i] % 2 != 0 and numbers[i] > numbers[i - 1]:
            series_counter += 1
        elif numbers[i] % 2 != 0:
            series_counter = 1
        else:
            series_counter = 0
        # checks if the size of the series that we have found is bigger than what we have found
        if series_counter > long_series and series_counter > 1:
            long_series = series_counter
        # if the number is even - we init the counter for the next iteration
    if series_counter > long_series and series_counter > 1:
        long_series = series_counter
    if long_series == 1:
        long_series = 0
    return long_series


def max_series(numbers):
    # This function uses 2 functions of odd series and divided in 3. The function return the value as a list of  results
    if not numbers:
        return numbers
    res = [odd_range(numbers), max_number_divide_3(numbers)]
    return res
