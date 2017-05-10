import string
import urllib.request
def remove_punctuation(str):
    for c in string.punctuation:
        str=str.replace(c,"")
    return str
url="http://cs1110.cs.virginia.edu/files/words.txt"
data=urllib.request.urlopen(url).read()
#print(data)
txt=data.decode("utf-8")
#print(txt)
dictionary=txt.split("\n")
dictionary=dictionary[:-1]
#print(dictionary[-1])
line=input("Type text;enter a blank line to end\n")
while line:
    word_list=remove_punctuation(line).split()
    for word in word_list:
        if word not in dictionary:
            print("MISSPELLED:{}".format(word))
