import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefings-statements/")
src = result.content
soup = BeautifulSoup(src, 'lxml')

urls = []
for h2 in soup.find_all("h2"):
    a = h2.find('a')
    urls.append(a.attrs['href'])

for link in urls:
    print(link)
