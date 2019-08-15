'''
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.


'''

def find_short(s):
    strSplit = s.split(" ")
    strLower=[]
    for i in strSplit:
        strLower.append(len(i))
    l = min(strLower)
    return l # l: shortest word length
    
