# a,b = 0,1
# for i in range(0,10):
#     print a
#     a,b = b, a+b
#
#
# my_list = [1,2,3,4,5,6,7,8,9,10]
#
# squares = [num*num for num in my_list]
# print squares
#
# import mem_profile
# from bs4 import BeautifulSoup
#
# import requests
# import sys
#
# url = 'http://www.imdb.com/chart/top'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "lxml")
# tr = soup.findChildren("tr")
# tr = iter(tr)
# next(tr)
# # print soup.findChildren("tr")
# for movie in tr:
#     title = movie.find('td', {'class': 'titleColumn'} ).find('a').contents[0]
#     year = movie.find('td', {'class': 'titleColumn'} ).find('span', {'class': 'secondaryInfo'}).contents[0]
#     rating = movie.find('td', {'class': 'ratingColumn imdbRating'} ).find('strong').contents[0]
#     row = title + ' - ' + year + ' ' + ' ' + rating
#
# print(row)
