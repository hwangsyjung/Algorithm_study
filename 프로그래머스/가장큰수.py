from itertools import permutations
def solution(numbers):
    answer = ''
    lst = []
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x: x*3, reverse = True)
    return str(int(''.join(numbers)))