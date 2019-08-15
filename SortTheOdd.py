'''
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

'''

def sort_array(source_array):
    if source_array == []:
        return []
    odds = iter(sorted(x for x in source_array if x % 2))
    return [next(odds) if x % 2 else x for x in source_array]
