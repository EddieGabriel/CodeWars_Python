'''
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

'''

def find_it(seq):
    count = 0
    for item in set(seq):
        print("(",item,")")
        for i in seq:
            if i == item:
                count += 1
        if count % 2 != 0:
            return item
        print(count)
