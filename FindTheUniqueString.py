'''

There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'

Strings may contain spaces. Spaces is not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 3 strings.

'''

def find_uniq(arr):
    a = []
    b = []
    for i in arr:
        a.append(''.join(sorted(i.lower())).strip())
    for i in a:
        b.append(''.join(set(list(i))).strip())
    c = [i for i in b if b.count(i)==1]

    for i in range(0,len(b)):
        if b[i] == c[0]:
            return arr[i]
