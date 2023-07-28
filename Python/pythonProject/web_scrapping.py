import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as bs


# Making a GET request
# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
#
# # check status code for response received
# # success code - 200
# print(r)
#
# # Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())

# Making a GET request
r = requests.get('https://www.amazon.in/New-Apple-iPhone-12-64GB/dp/B08L5W16HX/ref=sr_1_1_sspa?crid=ABWNM8M49BG5&keywords=iphone+12&qid=1686029784&sprefix=iphone+1%2Caps%2C213&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.find('div'))


# find all the anchor tags with "href"
# for link in soup.find_all('p'):
# 	print(link.get('style'))
# 	print(soup.findAll)

# Making a GET request
#r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')
#
# images_list = []
# #
# images = soup.select('img')
# for image in images:
# 		src = image.get('src')
# 		alt = image.get('alt')
# 		images_list.append({"src": src, "alt": alt})
# #
# for image in images_list:
#     print(image)


# URL = 'https://www.geeksforgeeks.org/page/1/'
#
# req = requests.get(URL)
# soup = bs(req.text, 'html.parser')
#
# titles = soup.find_all('div',attrs = {'class','head'})
#
# print(titles[1].text)
texts = soup.find_all('p')
for text in texts:
    print(text.get_text())

