'''
Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

The keypad has the following layout:

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘

He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java and C#) of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.

Detective, we count on you!

'''

def get_pins(observed):
numpad = [[0,8],[1,2,4],[1,2,3,5],[2,3,6],[1,4,5,7],[2,4,5,6,8],[3,5,6,9],[4,7,8],[0,5,7,8,9],[6,8,9]]

    list_observed = [int(x) for x in str(observed)]

    if len(list_observed) == 1:
        return numpad[observed]

    result = []
    for i in range(0,len(list_observed)):
        a=[]
        for j in range(0,len(list_observed)):
            if j != i:
                a.append(list_observed[j])
        for x in numpad[int(list_observed[i])]:
            y=[]
            y.append(x)
            for k in a:
                y.append(k)
            result.append(''.join(str(v) for v in y))
    return result
  
  
