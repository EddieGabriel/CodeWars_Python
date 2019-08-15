'''
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']

'''

def solution(s):
    a=[]
    if len(s) % 2 != 0 : s+='_'
    for i in range(len(s)):
        if i%2==0: a.append(s[i]+s[i+1])
    return a
