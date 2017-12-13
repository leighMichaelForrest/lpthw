import requests
import json
import wikipedia
import random


def astros():
    """Call the api and get a list of astronauts/cosmonauts."""
    astros = []

    # get the list and convert it to dictionary
    astros_raw = requests.get('http://api.open-notify.org/astros.json')
    astro_dict = json.loads(astros_raw.text)

    # process the names in the dictionary
    for astro in astro_dict['people']:
        # if name ends in 'kiy', replace with 'ky'; replace spaces with underscore
        name = astro['name'].replace('kiy', 'ky').replace(' ', '_').lower()
        astros.append(name)

    return astros


def astro_image(astro_wiki):
    """"Get an image of an astronaut """
    images = astro_wiki.images
    # todo get a whitelist of images
    images = [img for img in images if img.endswith('.jpg')]
    return random.choice(images)


def home_data():
    """Get data for the homepage."""
    # array for homepage
    astro_list = []
    # get list of astronauts from the api
    astronauts = astros()

    # process the list of astronauts
    for astro in astronauts:
        astro_wiki = wikipedia.page(astro)
        astro_dict = {}
        astro_dict['link'] = '/' + astro
        astro_dict['name'] = astro.replace('_', ' ').title()
        astro_dict['image'] = astro_image(astro_wiki)
        astro_list.append(astro_dict)

    return astro_list


def detail_data(astro):
    # get list of valid data
    astro_list = astros()

    # get a dictionary for the entry
    astro_data = astro_wiki(astro_list, astro)
    return astro_data


def astro_wiki(lyst, astro):
    """Get dictionary of wikipedia data of astro."""
    astro_dict = {}

    try:
        # if astronaut is in space, get image, summary, and link
        if astro in lyst:
            astro_wiki = wikipedia.page(astro)
            astro_dict['name'] = astro.replace('_', ' ').title()
            astro_dict['summary'] = wikipedia.summary(astro)
            astro_dict['url'] = astro_wiki.url
            # strip out bad images (.svg) and pick random one
            # todo: get a whitelist of images
            astro_dict['image'] = astro_image(astro_wiki)
        else:
            raise ValueError
    # Handle exceptions
    except wikipedia.exceptions.DisambiguationError:
        print("Multiple entries.")

    except wikipedia.exceptions.PageError:
        print("Page not found.")

    except ValueError:
        print("Value not valid.")

    finally:
        return astro_dict


if __name__ == '__main__':
    print(home_data())
