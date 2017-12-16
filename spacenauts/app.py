from flask import Flask
from flask import render_template
from astronauts.astros import Astronauts
app = Flask(__name__)
astros = Astronauts()

@app.route('/')
def home():
    """The home route. Display image and name of astronaut/cosmonaut."""
    astronauts = astros.get_index_data()
    return render_template("index.html", astronauts=astronauts)

@app.route('/<string:astronaut>')
def detail_astronaut(astronaut):
    """Displays wikipedia data on astronaut."""
    astros.get_astros()
    astro_data = astros.astro_wiki(astronaut)
    return render_template("detail.html", astro_data=astro_data)

if __name__ == '__main__':
    app.run()
