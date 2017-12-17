from bs4 import BeautifulSoup

import requests

BASE_URL = 'https://www.billboard.com'

def get_next_week(soup):
    """Get the link for the chart for the following week."""
    if soup.__class__.__name__ == "BeautifulSoup":
        # if soup is in fact BeautifulSoup, get the nav links
        links = soup.findAll('a', {'class': 'chart-nav__link'})
        if len(links) == 2:
            return "{}{}".format(BASE_URL, links[1]['href'])
        else:
            return None
    else:
        return None


def get_weeks_chart(soup):
    """Gets the chart data for the week in the soup."""
    chart = []

    if soup.__class__.__name__ == "BeautifulSoup":
        # get the song data soup
        songs = soup.findAll('article', {'class': 'chart-row'})
        # loop through the songs to get the data
        for song in songs:
            # create data dictionary for each song
            entry_dict = {}
            # get position
            position = song.find('span', {'class': 'chart-row__current-week'})
            entry_dict['position'] = position.get_text().lower()

            # get song
            chart_song = song.find('h2', {'class': 'chart-row__song'})
            entry_dict['chart_song'] = chart_song.get_text().lower()

            # get artist Not all artists have links
            artist = song.find('a', {'class': 'chart-row__artist'})
            if artist:
                entry_dict['artist'] = artist.get_text().strip().lower()
            else:
                artist = song.find('span', {'class': 'chart-row__artist'})
                entry_dict['artist'] = artist.get_text().strip().lower()

            # add dict to chart list
            chart.append(entry_dict)

        # return the chart data
        return chart
    else:
        return None

if __name__ == '__main__':
    url = 'https://www.billboard.com/charts/hot-100/2017-11-02'

    while url:
        # get data
        data = requests.get(url).text
        # make soup
        soup = BeautifulSoup(data, "html.parser")
        # get chart data here
        chart = get_weeks_chart(soup)
        for song in chart:
            print(song)
        url = get_next_week(soup)
        print(url)
