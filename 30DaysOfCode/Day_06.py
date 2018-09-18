#!/bin/python3

if __name__ == '__main__':
    T = int(input())
    odd_string, even_string = '', ''
    for i in range(T):
        S = input()
        odd_string = ''.join(S[0:len(S):2])
        even_string = ''.join(S[1:len(S):2])
        print(odd_string, even_string)