def ReverseWords(input:str):
    x=input.split(" ")
    lenX=len(x)
    # print(x[::-1])
    return ' '.join(x[::-1])

def rev_sentence(sentence):
 
    # first split the string into words
    words = sentence.split(' ')
 
    # then reverse the split string list and join using space
    reverse_sentence = ' '.join(reversed(words))
 
    # finally return the joined string
    return reverse_sentence

print(ReverseWords("geeks quiz practice code"))
