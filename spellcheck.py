import string
def remove_punctuation(str):
    for c in string.punctuation:
        str=str.replace(c,"")
    return str

dictionary=[]
with open("words.txt") as f:
    for line in f:
        dictionary.append(line)
line=input("Type text;enter a blank line to end\n")
while line:
    word_list=remove_punctuation(line).split()
    for word in word_list:
        if word not in dictionary:
            print("MISSPELLED:{}".format(word))
