#!/bin/python3

if __name__ == '__main__':
    N = int(input())
    return_string = ''
    if N % 2 == 0:
        if (N >= 2 and N <= 5) or N > 20:
            return_string = 'Not Weird'
        elif N >= 6 and N <= 20:
            return_string = 'Weird'
    else:
        return_string = 'Weird'
    print(return_string)