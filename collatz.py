import sys


def collatz(n):
    if n % 2 == 0:
        n = n // 2
        return n
    elif n % 2 == 1:
        n = 3 * n + 1
        return n


def validate(inp):
    try:
        int(inp) + 1.0
        return int(inp)
    except ValueError:
        if inp == 'exit':
            return inp
        else:
            print('That\'s not an integer. Enter a whole number with no decimals.')
            return 0

while True:
    print('Enter an integer and see the Collatz sequence at work (or type \'exit\' to quit).')
    num = validate(input())
    if num == 'exit':
        sys.exit()
    elif num == 0:
        continue
    while num != 1:
        if collatz(num) == 1:
            print(collatz(num))
        else:
            print(collatz(num), end=',')
        num = collatz(num)
    print('\n')
