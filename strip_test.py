import string

def remove_punctuation(str):
    for c in string.punctuation:
        str=str.replace(c,"")
    return str
line=input("Enter a sentence:")
word_list=remove_punctuation(line).split()
print(word_list)
