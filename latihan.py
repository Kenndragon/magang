def reverse_sentence(sentence):
    word = sentence.split()[::-1]
    string = ""
    for i in word:
        string = string + i + " "
    return string


sentence = input()
print(reverse_sentence(sentence))

