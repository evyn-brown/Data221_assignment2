import string
from collections import Counter, defaultdict

#open given file in write mode
file = open(file="sample-file.txt", mode="r")

#new list to store all cleaned lines from file
cleanedLines=[]

#create empty dictionary to store line num of similar lines
line_numbers=defaultdict(list)
#iterate through each line in the fil
for line_num, line in enumerate(file, start=1):
    #strip whitespace
    newLine=line.strip()
    #remove punctuation
    stringNoPunctuation=newLine.translate(str.maketrans('','',string.punctuation))
    #remove space between words
    tokens="".join(stringNoPunctuation.split())
    #make the line lowercase
    tokens=tokens.lower()

    if tokens:
        #append the clean line to tokens
        cleanedLines.append(tokens)
        #empty append line number of line to line_numbers
        line_numbers[tokens].append(line_num)

#count occurance of each line in list
lines_count=Counter(cleanedLines)

#create new list to store duplicate lines
duplicateLines=[]

for lines, count in lines_count.items():
    #if the line occures more than once...
    if count>1:
        #append line to duplicate line list
        duplicateLines.append(lines)


#get and print length of list of duplicate lines
duplicateCount=len(duplicateLines)
print(f"Count of near-duplicate lines: {duplicateCount}\n")



print("first two near-duplicate lines: ")
#get and print the first two duplicate lines and their line number
for i in range (min(2, duplicateCount)):
    line=duplicateLines[i]
    print(f"{line_numbers[line]} -> {line}")


