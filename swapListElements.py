def swapListElements(numList, j, k):
    newList = numList[:]         
    newList[j], newList[k] = newList[k], newList[j] 
    return newList
sampleList = [1, 2, 3, 4, 5]
print("list length: ", len(sampleList))
print("swap: ",swapListElements(sampleList, 1, 3))  