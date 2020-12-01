# Good morning! Here's your coding interview problem for today.

# This problem was asked by Nest.

# Create a basic sentence checker that takes in a stream of characters and determines whether they form valid sentences. If a sentence is valid, the program should print it out.

# We can consider a sentence valid if it conforms to the following rules:

#     The sentence must start with a capital letter, followed by a lowercase letter or a space.
#     All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
#     There must be a single space between each word.
#     The sentence must end with a terminal mark immediately following a word.

terminal_marks = ['.', '?', '!', '‽']
seperator_marks = [',', ';', ':']

def start(sentence:str) -> bool:
    "Return True if the first letter is Uppercase and the second character is a space or lowercase"
    first = sentence[0:1].isupper() 
    second = sentence[1:2].islower() or sentence[1:2] == ' '
    return(first and second)

def others(sentence:str) -> bool:
    "Return True if all characters in the string apart from the first are lowercase, or terminal or seperator marks"
    for i in sentence[3:]:
        if not (i.islower() or (i in terminal_marks) or (i in seperator_marks)):
            return False
        return True

def spaces(sentence:str) -> bool:
    "Return True if all words are seperated by a single space"
    words = sentence.split(' ')
    unstripped = [x == '' for x in words]
    return False if any(unstripped) else True

def ending(sentence:str) -> bool:
    "Return True if sentence ends with a valid terminal mark"
    return(sentence[-1:] in terminal_marks)

def is_valid_sentence(sentence: str) -> bool:
    "Returns True if str `sentence` is a sentence s.t. it follows the structural rules."
    return all([start(sentence), others(sentence), spaces(sentence), ending(sentence)])

if __name__ == "__main__":

    # Passing example
    ex = "I hope this, my example, is a good example of a valid sentence!"
    print(f"is_valid_sentence: {is_valid_sentence(ex)}") # is_valid_sentence: True
    print(f"start: {start(ex)}") # start: True
    print(f"others: {others(ex)}") # others: True
    print(f"spaces: {spaces(ex)}") # spaces: True
    print(f"ending: {ending(ex)}") # ending: True

    fail = "hello This sentence has a   leading lowercase and a double space and no terminal mark"
    print(f"is_valid_sentence: {is_valid_sentence(fail)}") # is_valid_sentence: False
    print(f"start: {start(fail)}") # start: False
    print(f"others: {others(fail)}") # others: True
    print(f"spaces: {spaces(fail)}") # spaces: True
    print(f"ending: {ending(fail)}") # ending: False