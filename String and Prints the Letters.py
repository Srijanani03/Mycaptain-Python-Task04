string=input("Enter a string: ")
def make_dict(x):
    dictionary = {}
    for letter in x:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary

def countchars(string):
    letters = [letter.lower() for letter in string if letter.isalpha()]
    dictionary = make_dict(letters)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print (letter,"=",count, end="   ")
countchars(string)
