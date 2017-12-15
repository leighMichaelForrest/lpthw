import unittest
import mock
import unittest
import json
import wikipedia

from astronauts import Astronauts


class MockWiki(object):
    """An ojbect inteded to mock the wikipedia module calls."""
    def __init__(self, name):
        self.name = name
        self.url = "http://google.com"
        self.images = ['https://upload.wikimedia.org/wikipedia/commons/7/73/Blue_pencil.svg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Expedition_5_EVA.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/e/ec/Expedition_5_EVA.jpg']

    @classmethod
    def page(self, item):
        return MockWiki(item)


# Dummy api data
ASTRONAUTS = """
    {"number": 5, "message": "success", "people": [
    {"name": "Sergey Ryazanskiy", "craft": "ISS"},
    {"name": "Randy Bresnik", "craft": "ISS"},
    {"name": "Alexander Misurkin", "craft": "ISS"},
    {"name": "Mark Vande Hei", "craft": "ISS"},
    {"name": "Joe Acaba", "craft": "ISS"}]}
"""

# Dummy list of astronauts/cosmonauts in space.
ASTRO_LIST = ['sergey_ryazansky', 'randy_bresnik', 'alexander_misurkin', 'mark_vande_hei', 'joe_acaba']

# Dummy data dictionary.
WIKI_DATA = {
    'name': 'randy_bresnik',
    'summary': "This is a journey into sound!",
    'url': 'http://google.com',
    'image': 'http://image.gift.jpg'
}

def summary(item):
    # item not used, this is mock data
    return "This is just dummy data. Go see wikipedia."

class AstronautTestCase(unittest.TestCase):
    def setUp(self):
        self.astronauts = Astronauts()
        self.url = url = 'http://api.open-notify.org/astros.json'


    @mock.patch('astronauts.requests.get')
    def test_get_ok(self, mock_get):
        """
            Test getting a 200 OK response from the _get method of Astronauts.
            The internal call to requests.get() is mocked.
        """
        # Construct our mock response object
        mock_response = mock.Mock()
        expected_dict = json.loads(ASTRONAUTS)
        mock_response.json.return_value = expected_dict

        # Assign our mock response as the result of our patched function
        mock_get.return_value = mock_response

        url = self.url
        response_dict = self.astronauts._get(url=url)

        # Check that our function made the expected internal calls
        mock_get.assert_called_once_with(url=url)
        self.assertEqual(1, mock_response.json.call_count)

        # If we want, we can check the contents of the response
        self.assertEqual(response_dict, expected_dict)

    @mock.patch.object(Astronauts, '_get')
    def test_astronauts(self, mock_get):
        """Test a call to get_astros. Mocks the method ._get()"""
        mock_get.return_value = json.loads(ASTRONAUTS)

        astros = Astronauts()
        lyst = astros.get_astros()
        mock_get.assert_called_once()
        self.assertEqual(ASTRO_LIST, lyst)


    @mock.patch('wikipedia.summary')
    @mock.patch('wikipedia.page')
    def test_astro_wiki(self, mock_wiki, mock_summary):
        """Test for the return of dictionary."""
        self.astronauts.astros = ASTRO_LIST
        test_astro = 'randy_bresnik'

        # make a mock of wikipedia.page() data
        mock_wiki.return_value = MockWiki.page(test_astro)
        mock_instance = mock_wiki.return_value

        mock_summary.side_effect = summary(test_astro)

        # run method
        astro_dict = self.astronauts.astro_wiki(test_astro)

        # test for method call
        mock_wiki.assert_called_once_with(test_astro)
        mock_summary.assert_called_once_with(test_astro)

        # assert for data
        self.assertIn('name', astro_dict)
        self.assertIn('summary', astro_dict)
        self.assertIn('url', astro_dict)
        self.assertIn('image', astro_dict)


    def test_astro_not_in_space(self):
        """Test for the return of blank dictionary."""
        # don't mock.... put fake data in directly.
        self.astronauts.astros = ASTRO_LIST
        test_astro = 'turtle_newman'

        astro_dict = self.astronauts.astro_wiki(test_astro)
        # assert for data
        self.assertEqual({}, astro_dict)

    @mock.patch('wikipedia.page')
    def test_astro_wiki_bad_page_error(self, mock_wiki):
        """Test for the return of dictionary."""
        self.astronauts.astros = ASTRO_LIST
        test_astro = 'randy_bresnik'

        # the method raises exception
        mock_wiki.side_effect = wikipedia.exceptions.PageError

        # run method
        astro_dict = self.astronauts.astro_wiki(test_astro)

        # test for method call
        mock_wiki.assert_called_once_with(test_astro)

        self.assertEqual({}, astro_dict)

    @mock.patch('wikipedia.page')
    def test_astro_wiki_disambiguation_error(self, mock_wiki):
        """Test for the return of dictionary."""
        self.astronauts.astros = ASTRO_LIST
        test_astro = 'randy_bresnik'

        # the method raises exception
        mock_wiki.side_effect = wikipedia.exceptions.DisambiguationError

        # run method
        astro_dict = self.astronauts.astro_wiki(test_astro)

        # test for method call
        mock_wiki.assert_called_once_with(test_astro)

        self.assertEqual({}, astro_dict)


    def test_get_astro_image(self):
        """Test return of image."""
        test_astro = 'randy_bresnik'
        astro = MockWiki.page(test_astro)
        image = self.astronauts.get_astro_image(astro.images)
        self.assertIsNotNone(image)

    def test_get_astro_image_is_none(self):
        """Test un-return of image."""
        test_astro = 'turtle_newman'
        astro = MockWiki.page(test_astro)
        image = None
        self.assertIsNone(image)

    @mock.patch.object(Astronauts, 'astro_wiki')
    @mock.patch.object(Astronauts, 'get_astros')
    def test_get_index_data(self, mock_astros, mock_wiki):
        # Set the return values with dummy data
        mock_astros.return_value = ASTRO_LIST
        mock_wiki.return_value = WIKI_DATA

        # make working object
        astros = Astronauts()

        # call the function
        astro_list = astros.get_index_data()
        number_astros = len(astro_list)
        # see if the mocked function was called
        mock_astros.assert_called_once()
        # make sure that the number of astro_wiki() calls equals
        #    number of astros
        self.assertEqual(mock_wiki.call_count, number_astros)
        self.assertEqual(len(astro_list), len(ASTRO_LIST))

if __name__ == "__main__":
    unittest.main()
