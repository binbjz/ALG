#!/usr/bin/env python
#filename: binary_search.py
#

def search(arr,n,v):
    left = -1
    right = n

    while(left+1 != right):
        mid = left+(right-left)/2
        if(arr[mid] < v):
            left = mid
        else:
            right = mid

    if(right >= n or arr[right] != v):
        right = -1

    return right


if __name__ == '__main__':
    arr = [12,1,26,2,4,62,23,87,90,555,1222,126,1444,621]
    arr.sort()
    n = len(arr)

    ret = search(arr, n, 87)
    print 'array: ', arr
    print 'binary search--value index: ', ret
