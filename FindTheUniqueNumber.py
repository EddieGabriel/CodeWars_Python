'''

There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

It’s guaranteed that array contains more than 3 numbers.

The tests contain some very huge arrays, so think about performance.

'''
#my solution

def find_uniq(arr):
    s = set(arr)
    for i in s:
        x = arr.count(i)
        if x == 1:
            return i

#def find_uniq(arr):
#    a, b = set(arr)
#    return a if arr.count(a) == 1 else b
