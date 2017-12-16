import requests
import json
import wikipedia
import random


class Astronauts(object):
    url = 'http://api.open-notify.org/astros.json'

    def __init__(self):
        self.astros = []

    def _get(self, url):
        """Get json from the request."""
        response = requests.get(url=url)
        return response.json()

    def get_astros(self, url=url):
        """Return a list of active astronauts."""
        if self.astros == []:
            # get astros json object
            astro_dict = self._get(url=url)

            # process the astros
            for astro in astro_dict['people']:
                #if name ends in 'kiy', replace with 'ky'; replace spaces with underscore
                    name = astro['name'].replace('kiy', 'ky').replace(' ', '_').lower()
                    self.astros.append(name)

        return self.astros

    def get_index_data(self):
        """Get the data needed for the homepage"""
        astro_data = []
        # get the list of astronauts
        astros = self.get_astros()
        # get a dict for each astronaut in the list
        for astro in astros:
            astro_dict = self.astro_wiki(astro)
            astro_data.append(astro_dict)
        print(astro_data)
        return astro_data

    def get_astro_image(self, images):
        """Return one image from a list of images."""
        images = [img for img in images if img.endswith('.jpg')]
        return random.choice(images)

    def astro_wiki(self, astro):
        """Get data on an astronaut from wikipedia."""
        astro_dict = {}

        try:
            # If astronaut is in the list of active astronauts, write the dict.
            if astro in self.astros:
                astro_wiki = wikipedia.page(astro)
                astro_dict['url_name'] = astro
                astro_dict['name'] = astro.replace('_', ' ').title()
                astro_dict['summary'] = wikipedia.summary(astro)
                astro_dict['url'] = astro_wiki.url
                astro_dict['image'] = self.get_astro_image(astro_wiki.images)
            else:
                raise ValueError
        except ValueError:
            print(f"{astro} is not in space.")
        except wikipedia.exceptions.PageError:
            print("Page not found.")
        except wikipedia.exceptions.DisambiguationError:
            print("Too many entries.")
        finally:
            return astro_dict
