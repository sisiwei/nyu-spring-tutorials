# Let's scrape this website
import requests
import csv
from BeautifulSoup import BeautifulSoup

url = "http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp"

# Open the HTML file and turn it into a BeautifulSoup object for parsing
r = requests.get(url)
content = r.content
soup = BeautifulSoup(content)

# The scrape actually starts here.
# Let's get the table that contains the results.
results_table = soup.find("table", attrs={"class": "resultsTable"})
rows_list = results_table.findAll('tr')

all_output = []

for row in rows_list:
	if row == rows_list[0]:
		td_list = row.findAll("th")
	else:
		td_list = row.findAll("td")

	all_column_data = []

	for column in td_list:
		text = column.text.replace("&nbsp;", "")
		all_column_data.append(text)

	all_output.append(all_column_data)

csv_file = open('inmates-today.csv', 'w')
outfile = csv.writer(csv_file)
outfile.writerows(all_output)

print "I think I'm done."

# rows_list = [
# 	["<td>Young</td>", "<td>James</td>", "<td>Arthur</td>"], 
# 	["<td>Wei</td>", "<td>Sisi</td>", "<td></td>"]
# ]

# sample_list = [["sisi", "teacher"], ["madeline", "student"], ["eric", "student"]]

# for list_item in sample_list:
# 	print list_item[0]
	# for person in list_item[0]:
	# 	print person

# print sample_list

