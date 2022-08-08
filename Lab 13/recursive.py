# 12. Given a list of integers a1, ..., an.
# Determine all the possibilities of inserting '+' and '-' between the numbers
# for the result of the expression to be >= 0
# recursive BACKTRACKING solution

def expr_res(stack, array):
    x = array[0]
    index = 1
    for sign in stack:
        if sign == "-":
            x -= array[index]
        else:
            x += array[index]
        index += 1
    return x


def print_solution(stack, array):
    print_string = str(array[0])
    index = 1
    for sign in stack:
        print_string += sign + str(array[index])
        index += 1
    print_string += '=' + str(expr_res(stack, array))
    print(print_string)


def solution(stack, array):
    x = expr_res(stack, array)
    if x < 0:
        return False
    return True


def backtracking(k, stack, array):
    signs = ["-", "+"]
    solutions = 0
    for sign in signs:
        # we put the signs in the stack
        stack.append(sign)
        # if we inserted n-1 signs we check if it's a valid solution
        if k == len(array)-1:
            if solution(stack, array):
                print_solution(stack, array)
                solutions += 1
        else:
            solutions += backtracking(k+1, stack, array)
        del stack[-1]
    return solutions


def main():
    input_array = input("Enter numbers separated by spaces: ").split()
    numbers_array = []
    for number in input_array:
        numbers_array.append(int(number))
    stack = []
    backtracking(1, stack, numbers_array)


main()
