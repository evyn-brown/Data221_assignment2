from bs4 import BeautifulSoup
import requests


#beautiful soup formats
header={"User-Agent": "Mozilla/5.0"}
#request accesses webpage
wikipedia = requests.get("https://en.wikipedia.org/wiki/Data_science", headers=header)
parsedDoc=BeautifulSoup(wikipedia.content, "html.parser")

#find all finds instance of text type and adds them to a list
title = parsedDoc.title.string

#find main content area
content= parsedDoc.find('div', id='mw-content-text')

#empty list to store filtered headers
filteredHeaders=[]
#list of keywords
keyWord=["references","external links","see also","notes"]

#iterate through all headers in main content area
for h2 in content.find_all('h2'):
    #skip over modified headers
    edit=h2.find('span', class_='mw-editsection')
    if edit:
        edit.decompose()

    #get text of header
    header=h2.get_text(strip=True)

    #if keywords are not in header
    if not any(word in header.lower() for word in keyWord):
        #append header to filtered header
        filteredHeaders.append(header)

#write to new file
file = open("headings.txt", "w")
#write each item in filtered headers on a new line
for heading in filteredHeaders:
    file.write(heading + "\n")