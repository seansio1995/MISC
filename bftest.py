from bs4 import BeautifulSoup
import requests
#soup = BeautifulSoup(login_page.text,"html.parser")
session=requests.Session()
login_page = session.get('http://uva.onlinejudge.org/')
soup = BeautifulSoup(login_page.text,"html.parser")
inputs = soup.find('form', attrs={'id': 'mod_loginform'}).find_all('input')
print(inputs)
