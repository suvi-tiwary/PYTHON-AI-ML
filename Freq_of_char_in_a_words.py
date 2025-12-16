'''
Write a Python function to count the frequency of each character in a
given string and return the output in a dictionary
'''
freq = {}
word = input("Enter the word: ")

char = 0
while char < len(word):
    ch = word[char]
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
    char += 1

print(freq)


