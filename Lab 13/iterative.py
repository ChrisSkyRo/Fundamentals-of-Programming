# 12. Given a list of integers a1, ..., an.
# Determine all the possibilities of inserting '+' and '-' between the numbers
# for the result of the expression to be >= 0
# iterative BACKTRACKING solution

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


def backtracking(array):
    solutions = 0
    stack = ["-"]  # we initialize the stack with a minus
    while len(stack) > 0:
        # if we inserted n-1 signs we check if it's a valid solution
        if len(stack) == len(array)-1:
            if solution(stack, array):
                print_solution(stack, array)
                solutions += 1
            # we remove all pluses until we reach a minus or the stack is empty
            while len(stack) > 0 and stack[-1] == '+':
                del stack[-1]
            # if the stack isn't empty the rightmost minus becomes a plus
            if len(stack) > 0:
                stack[-1] = "+"
        else:
            stack.append("-")
    return solutions


def main():
    input_array = input("Enter numbers separated by spaces: ").split()
    numbers_array = []
    for number in input_array:
        numbers_array.append(int(number))
    backtracking(numbers_array)


main()
