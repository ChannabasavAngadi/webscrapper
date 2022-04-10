import requests
from bs4 import BeautifulSoup

html = requests.get('https://courses.ineuron.ai/category/Data-Science').text
soup = BeautifulSoup(html,'lxml')
for i in soup.find_all('div', class_='Course_flex__3ZrIo flex'):
    anchor = i.find('h5')
    print(anchor.text)