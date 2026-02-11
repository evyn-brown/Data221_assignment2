import string
from collections import Counter

#open given file
file = open(file="sample-file.txt", mode="r")

#create empty list for all processed words
processedToken=[]

#iterate through each line in the file
for line in file:
    #strip the line of whitespace
    newLine=line.strip()
    #remove punctuation
    stringNoPunctuation=newLine.translate(str.maketrans('','',string.punctuation))
    #seperate words into token list
    tokens=stringNoPunctuation.split()

    #for each token (word in line)
    for token in tokens:
        #make the word lowercase
        token=token.lower()
        if len(token)>1:
            #add token to token list if it has more than one character
            processedToken.append(token)

#count occurences of each processed token in token list
wordCount=Counter(processedToken)
#get top ten occuring words into new list
top10=wordCount.most_common(10)


print("10 most frequent words: ")
#iterate through each item in top 10 list
for item in top10:
    #print word and word count
    print(f"{item[0]} -> {item[1]}")





