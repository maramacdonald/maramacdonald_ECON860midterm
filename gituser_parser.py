from bs4 import BeautifulSoup
import os

import pandas 

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

df = pandas.DataFrame()

file_name = "html_files/gitusers.html"
f = open(file_name, "r")
soup = BeautifulSoup(f.read(), "html.parser")
f.close()


soup2 = soup.find_all("div")

for divs in range(len(soup2)):
	if divs > 3:
		gitname = soup2[divs]["ghid"]
		df = df.append({'ghid': gitname}, ignore_index = True)
		#print(df.loc[divs-4])
#print(len(df))
df.drop_duplicates(subset="ghid", keep='first', inplace=True)

print(len(df))

df.to_csv("parsed_files/gitusersdata.csv", index=False)
print("done")
