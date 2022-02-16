import requests
from bs4 import BeautifulSoup
import csv

url = "http://nepalstock.com/indices"

r = requests.get(url)
html_content = r.content
soup = BeautifulSoup(html_content, 'html.parser')

file_name = 'scraped_stock_data.csv'
csv_writer = csv.writer(open(file_name,'w'))


title = soup.find('label',class_='pull-left') # title of the page as per my content 
print(title.text)


headings = soup.find('tr', class_="unique")
headings_lst = []   #table head comes here
for each_heading in headings.find_all('td'):
    headings_lst.append(each_heading.text.strip())
for_csv_data = headings_lst
csv_writer.writerow(for_csv_data)

print(headings_lst)

table = soup.find('table', class_="table table-condensed table-hover")
required_data = table.find_all('tr')[2:]

# print(required_data)
allrow = []
for each_td in required_data:
    data = []
    for each_data in each_td.find_all('td'):
        data.append(each_data.text.strip())
    for_csv_data = data
    csv_writer.writerow(for_csv_data)
    allrow.append(data)
print(allrow)
    





