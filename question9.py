from bs4 import BeautifulSoup
import requests
import pandas as pd

#beautiful soup formats
headers={"User-Agent": "Mozilla/5.0"}
#request accesses webpage
wikipedia = requests.get("https://en.wikipedia.org/wiki/Machine_learning", headers=headers)
soup=BeautifulSoup(wikipedia.content, "html.parser")
#access main content area
content=soup.find("div", id="mw-content-text")

#initialize main table to None
mainTable=None

#iterate through all tables within main content area
for table in content.find_all("table"):
    #find rows of the table
    rows=table.find_all("tr")
    #find table with more than 3 rows
    if len(rows)>=3:
        #assign main table
        mainTable=table
        break

#find headers of each row
headerRow=mainTable.find("tr")
#new empty list to store headers
headers=[]

#iterate through table headers of the main table
for th in table.find_all("th"):
    #get text of each header
    text=th.get_text(strip=True)
    #make header text or col(num) if unassigned
    headers.append(text if text else f"col{len(headers)+1}")

#empty list to store rows
rows=[]
#find number of cols by getting length of headers
maxCols=len(headers)

#iterate through table rows, excluding main columns headers
for tr in mainTable.find_all("tr")[1:]:
    #within rows, find all table data
    cells=tr.find_all("td")
    if not cells:
        continue

    #get and strip text, replace non breaking spaces with regular spaces
    row=[td.get_text(" ", strip=True).replace("\xa0", " ") for td in cells]
    maxCols=max(maxCols,len(rows))
    #append data to rows
    rows.append(row)

while len(headers)<maxCols:
    headers.append(f"col{len(headers)+1}")

for row in rows:
    while len(row) < maxCols:
        row.append("")

df=pd.DataFrame(rows, columns=headers)
df.to_csv('wiki_table.csv', index=False)