''' Write a function to find the longest word in a given list of words.
Example: longest_word([‘apple’, ‘banana’, ‘cherry’]) returns ‘banana’'''


def longest_word(l):
    longest=l[0]
    for word in l:
        if(len(longest)<len(word)):
           longest=word

    return longest

l=["apple","banana","cherry"]
result=longest_word(l)
print(result)       