'''
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
'''

def is_isogram(str):
        if str=="":
            return True
        else:
            a=[]
            b=str.lower()
            for x in b:
                a.append(b.count(x))
            if len(set(a))==1:
                return True
            else:
                return False
