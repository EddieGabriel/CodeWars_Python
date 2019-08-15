'''

You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block in a direction and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).


'''
# My Solution

def isValidWalk(walk):
    if len(walk) != 10: return False
    s = 0;n = 0; e = 0; w = 0
    for item in walk:
        if item == 's':
            s -= 1
            n += 1
        if item == 'n':
            s += 1
            n -= 1
        if item == 'e':
            w -= 1
            e += 1
        if item == 'w':
            e -= 1
            w += 1
    print(n,s,w,e)
    if s==0 and n==0 and w== 0 and e == 0:
        return True
    else:
        return False
        
#could be solved like this:def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
#def isValidWalk(walk):
#    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
