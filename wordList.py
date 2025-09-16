wordList = ["the", "cat", "in", "the", "hat", "is", "a", "great", "book"]
index = len(wordList) - 1
while index >= 0:
    if wordList[index] == "the" or wordList[index] == "a":
        wordList.pop(index)
    index -= 1

print(wordList)