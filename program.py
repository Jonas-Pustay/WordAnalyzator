import matplotlib.pyplot as plt
import numpy as np
import io

WordsToSearch = ["avec", "elle", "la", "il"]
WordsToCounts = [0] * len(WordsToSearch)

file = io.open("data.txt", mode="r", encoding="utf-8")
Words = file.read().split()

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