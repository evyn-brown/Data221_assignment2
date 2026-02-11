import string
from collections import Counter

#open given file as read mode
file = open(file="sample-file.txt", mode="r")

#create empty list to store processed tokens
processedToken=[]
#iterate through each line in file
for line in file:
    #strip whitespace
    newLine=line.strip()
    #remove punctuation
    stringNoPunctuation=newLine.translate(str.maketrans('','',string.punctuation))
    #seperate words into new list
    tokens=stringNoPunctuation.split()

    #iterate through word in line
    for token in tokens:
        #make word lowercase
        token=token.lower()
        if len(token)>1:
            #add word to list if length>1
            processedToken.append(token)

#new empty list to store bigrams
bigrams=[]
#for item in range 0, #words in processed tokens
for i in range(len(processedToken)-1):
    #append two consecutive words into bigram list
    bigrams.append((processedToken[i], processedToken[i+1]))

#count number of pairs in bigram list
bigram_count=Counter(bigrams)
#store top 10 pairs in new list
top10=(bigram_count.most_common(10))

print("10 most frequent bigrams: ")
#print the top ten bigrams and their count
for item in top10:
    print(f"{item[0][0]} {item[0][1]} -> {item[1]}")

