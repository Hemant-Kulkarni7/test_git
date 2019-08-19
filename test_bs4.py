from bs4 import BeautifulSoup # python3 -m pip install bs4
import requests # pip3 install requests
import sys

url = "http://www.codekul.com"
response = None

try:
    response = requests.get(url)
except Exception as e:
    print(repr(e))
    sys.exit(1)

if response.status_code != 200:
    print("Non success status code returned "+str(response.status_code))
    sys.exit(1)

soup = BeautifulSoup(response.content, 'html.parser')
#print(soup.prettify())

if soup.find("div", {"class": "errorpage-topbar"}):
    print("\n\n Error: Invalid username.")
    sys.exit(1)

links = soup.find_all("a")    

'''tweets = soup.find_all("p", {"target": "blank"})'''

linkList = []
for i in links:
    linkList.append(i)

for i in linkList:
    print(i.get('href'))

   