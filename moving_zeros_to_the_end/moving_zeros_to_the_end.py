a =  [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]

def move_zeros(lst):
    non_zeros = []
    zero_counter = 0

    for num in lst:
        if num != 0:
            non_zeros.append(num)
        else:
            zero_counter += 1
    result = non_zeros + [0] * zero_counter
    return result

def move_zero(array):
    for i in array:
        if i == 0:
            array.remove(i) # Remove the element from the array
            array.append(i) # Append the element to the end
    return array
print(move_zero1(a))
