#!/bin/python3

if __name__ == '__main__':  
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    for i in range(len(arr)):
        print(arr[len(arr) - i - 1], '', end='')