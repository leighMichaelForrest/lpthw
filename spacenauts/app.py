from flask import Flask
from flask import render_template
from astros import home_data, detail_data
app = Flask(__name__)

@app.route('/')
def home():
    astronauts = home_data()
    return render_template("index.html", astronauts=astronauts)

@app.route('/<string:astronaut>')
def detail_astronaut(astronaut):
    astronaut = detail_data(astronaut)
    return render_template("detail.html", astronaut=astronaut)

if __name__ == '__main__':
    app.run()
