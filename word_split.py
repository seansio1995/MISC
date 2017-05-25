def word_split(phrase,words_list,output=None):
    if output==None:
        output=[]
    for word in words_list:
        if phrase.startswith(word):
            output.append(word)

            return word_split(phrase[len(word):],words_list,output)
    return output


def testCase():
    assert word_split('themanran',['the','ran','man'])==['the', 'man', 'ran']
    assert word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])==['i', 'love', 'dogs', 'John']
    assert word_split('themanran',['clown','ran','man'])==[]

if __name__=="__main__":
    testCase()
