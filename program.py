import matplotlib.pyplot as plt
import numpy as np

WordsToSearch = ["Dieu", "elle", "la", "il","avec"]
WordsToCounts = [0] * len(WordsToSearch)

Words = open("data.txt","r",encoding='Latin1').read().split()

for Word in Words:
    for x in range(len(WordsToSearch)):
        if WordsToSearch[x] == Word.replace(",", "").replace(".", "").replace( ";","").replace("!","").replace("?","") :
            WordsToCounts[x] = WordsToCounts[x] + 1

WordToShowX = WordsToSearch
WordToShowY = WordsToCounts

for x in range(len(WordsToSearch)):
    print("Le mot ", WordsToSearch[x]," apparait ", WordsToCounts[x])

plt.bar(WordsToSearch,WordsToCounts)
plt.show()