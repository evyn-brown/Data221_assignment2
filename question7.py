from bs4 import BeautifulSoup
import requests


#beautiful soup formats
header={"User-Agent": "Mozilla/5.0"}
#request accesses webpage
wikipedia = requests.get("https://en.wikipedia.org/wiki/Data_science", headers=header)
parsedDoc=BeautifulSoup(wikipedia.content, "html.parser")

#find all finds instance of text type and adds them to a list
title = parsedDoc.title.string

#identify main content area
content= parsedDoc.find('div', id='mw-content-text')

#set variable for first paragraph
firstParagraph=None

#iterate through all paragraphs in content area
for p in content.find_all('p'):
    #get text of paragraph
    text=p.get_text()
    #strip whitespace
    text=text.strip()
    #if there are at least 50 characters,
    if (len(text))>50:
        #set as main paragraph
        firstParagraph=text
        break

#print title to user
print(f"Webpage Title: {title}")
#print first paragraph to user
print(f"First Paragraph: {firstParagraph}")