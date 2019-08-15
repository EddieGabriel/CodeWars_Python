'''
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false

Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

'''
# my solution

def anagrams(word, words):
    # Converting the string into a list, so i can sort it with the sort() method
    word_list = list(word)
    # Sorting the string
    word_list.sort()
    # Assign an empty list called result
    result = []
    
    # Here is the for so I can iterate in all of the "words" list
    # So, for each item I'll convert into a list, and them sort it.
    # if the sorted item is equal the word, then it's an anagrama
    for item in words:
        item_list = list(item)      # converting the list
        item_list.sort()            # sorting the word
        if word_list == item_list:  # if the word is equal to the item, then append to result
            result.append(item)
    return result                   # return result

