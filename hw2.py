# *************** HOMEWORK 2 ***************
# GOOD LUCK!

# ************************ QUESTION 1 **************************
# this function print triangle in vertical direction with given the size of the rows and the direction
def print_triangle(size, start, end, direction):
    asterisk = "*"
    back_space = ' '
    # prints over loop from start to end variable and prints backspace with asterisks
    for i in range(start, end, direction):
        print(back_space * (size - i) + asterisk * (2 * i - 1))


# this function print rhombus vertically using help function that prints 2 triangle in opposite directions
def rhombus(side_size):
    print_triangle(side_size, 1, side_size, 1)
    print_triangle(side_size, side_size, 0, -1)


# ************************ QUESTION 2 **************************
# this function gets a list and returns the list sorted from min to max value
def sort_list_min_to_max(list_numbers):
    for i in range(1, len(list_numbers)):
        for j in range(0, len(list_numbers) - i):
            # if the number is bigger than previous number that switch the indexes
            if list_numbers[j] > list_numbers[j + 1]:
                temp_num = list_numbers[j]
                list_numbers[j] = list_numbers[j + 1]
                list_numbers[j + 1] = temp_num
    return list_numbers


# this function find all combination of lagrange square of the num input
def lagrange_four_square_theorem(num):
    lagrange_list = []
    # find all the combination of 4 numbers until the sqrt of the number
    for i in range(int(num ** 0.5) + 1):
        for j in range(int(num ** 0.5) + 1):
            for k in range(int(num ** 0.5) + 1):
                for m in range(int(num ** 0.5) + 1):
                    if ((i ** 2) + (j ** 2) + (k ** 2) + (m ** 2)) == num:
                        # each combination get sorted by help function
                        temp_l = sort_list_min_to_max([i, j, k, m])
                        # insert all the combination that match without duplicates
                        if temp_l not in lagrange_list:
                            lagrange_list.append(temp_l)
    return lagrange_list


# ************************ QUESTION 3 **************************
# this function sort list from max to min value
def sort_list_max_to_min(list_numbers):
    for i in range(1, len(list_numbers)):
        for j in range(0, len(list_numbers) - i):
            # if the number is smaller than previous number that switch the indexes
            if list_numbers[j] < list_numbers[j + 1]:
                temp_num = list_numbers[j]
                list_numbers[j] = list_numbers[j + 1]
                list_numbers[j + 1] = temp_num
    return list_numbers


# This function get list of numbers and return the maximum number in the list that divide with 3
def max_number_divide_3(numbers):
    max_num = -1
    numbers = sort_list_max_to_min(numbers)
    for num in numbers:
        if num % 3 == 0 and num != 0:
            max_num = num
            break
    return max_num


# this function get a list and return the count of max range of odd numbers
def odd_range(num_list):
    counter = max_range = 0
    for i in range(len(num_list)):
        if num_list[i] % 2 != 0:
            if i == 0:
                counter += 1
            elif num_list[i] > num_list[i - 1]:
                counter += 1
            else:
                counter = 1
        else:
            counter = 0
        if counter > max_range:
            max_range = counter
    return max_range


# This function uses 2 functions of odd series and divided in 3. The function return the value as a list of  results
def max_series(numbers):
    if not numbers:
        return numbers
    res = [odd_range(numbers), max_number_divide_3(numbers)]
    return res
