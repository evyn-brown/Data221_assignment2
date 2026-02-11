
import string

#define funcioton
def find_lines_containing(filename, keyword):

    #open file
    file = open(filename, mode="r")
    #convert given keyword to lowercase
    keyword=keyword.lower()
    #new empty list to store lines with keywords
    line_with_keyword=[]

    #iterate through lines in file
    for line_num, line in enumerate(file, start=1):
        #remove punctuation and make line lowercase
        stringNoPunctuation = line.translate(str.maketrans("", "", string.punctuation)).lower()
        #make new list containing all word
        words = stringNoPunctuation.split()

        #if keyword is in list
        if keyword in words:
            #append keyword with line number
            line_with_keyword.append((line_num, line.rstrip()))

    #return list of keyword and line number
    return line_with_keyword

#sample file input and keyword to search
list_keywords=find_lines_containing("sample-file.txt", "lorem")
#return length of keywords
num_lines_found=len(list_keywords)
#print number of times keyword was listed in file
print(f"Your keyword was found {num_lines_found} times in the file")

#if word appears more than 3 times
if num_lines_found>=3:
    print("Printing first 3 occurrences of your keyword ...")

#print first three occurences of the word in file
for line_num, text in list_keywords[:3]:
    print(f"{line_num} -> {text}")