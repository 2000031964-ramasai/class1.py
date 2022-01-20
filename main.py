# cook your dish here
import numpy as np

arr = np.array([])

n = int(input())
while n > 0:
    size = int(input())
    for i in range(size):
        np.append(arr, input())
    max1 = arr[0]
    for i in range(size):
        if arr[i] > max1:
            max1 = arr[i]

    if max1 % 2 == 0:
        print(max1 + 2)
    else:
        print(max1 + 1)

    n = n - 1
    print("hello")



