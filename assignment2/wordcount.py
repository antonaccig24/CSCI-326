# Giorgio Antonacci
# wordcount.py

import os
import os.path

letters = "qwertyuiopasdfghjklzxcvbnm-123456789"

def openfile(filename):
    l = open(os.path.join(os.path.dirname(__file__), '..', 'datasets', filename), 'r', encoding="utf-8").read().lower()

    currentword = ""
    list_words = {}
    for i in l:
        if i in letters:
            if i != "-":
                currentword = currentword + i
        else:
            if currentword != "" and currentword != "s":
                if currentword in list_words:
                    list_words[currentword] += 1
                else:
                    list_words[currentword] = 1
                currentword=""

    f = open("freq_"+filename, 'w') 
    
    for i in range(0,50):
        word = max(list_words, key = list_words.get)
        f.write(word + " " + str(list_words[word]) +"\n")
        list_words[word] = 0
    f.close()

#openfile("descriptions.txt")
#openfile("headlines.txt")
#openfile("article_text.txt")
#openfile("cards.txt")