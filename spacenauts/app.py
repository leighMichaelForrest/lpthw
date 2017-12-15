from flask import Flask
from flask import render_template
from astronauts import Astronauts

app = Flask(__name__)
astros = astronauts.Astronauts()

@app.route('/')
def home():
    astronauts = astros.get_astros()
    return render_template("index.html", astronauts=astronauts)

@app.route('/<string:astronaut>')
def detail_astronaut(astronaut):
    astronaut = detail_data(astronaut)
    return render_template("detail.html", astronaut=astronaut)

if __name__ == '__main__':
    app.run()
