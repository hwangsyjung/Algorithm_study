n = int(input())
stack = []
idx = 1
for _ in range(n):
    num = int(input())
    while idx <= num:
        print('+')
        stack.append(idx)
        idx+=1
    if stack[-1] == num:
        print('-')
        stack.pop()
    else:
        print('No')
        exit(0)
print('\n'.join(result))