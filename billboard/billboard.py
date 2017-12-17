from bs4 import BeautifulSoup

import requests

BASE_URL = 'https://www.billboard.com'

def get_next_week(soup):
    if soup.__class__.__name__ == "BeautifulSoup":
        # if soup is in fact BeautifulSoup, get the nav links
        links = soup.findAll('a', {'class': 'chart-nav__link'})
        if len(links) == 2:
            return "{}{}".format(BASE_URL, links[1]['href'])
        else:
            return None
    else:
        return None

if __name__ == '__main__':
    url = 'https://www.billboard.com/charts/hot-100/2016-12-02'

    while url:
        # get data
        data = requests.get(url).text
        # make soup
        soup = BeautifulSoup(data, "html.parser")
        # to do: get chart data here
        url = get_next_week(soup)
        print(url)
