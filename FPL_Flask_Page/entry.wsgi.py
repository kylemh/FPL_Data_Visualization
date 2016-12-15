"""
Authors: Zoe Olson and Kyle Holmberg
Email: zoeo@cs.uoregon.edu or kmh@uoregon.edu

Flask front-end for MySQL database-driven visualizations and queries
"""
from flask import Flask, request, render_template
import pandas
from sqlalchemy import create_engine
import random


app = Flask(__name__)


@app.route('/')
def index():
	con = create_engine('mysql+pymysql://guest:guest@ix.cs.uoregon.edu:3640/fpl', echo=False)
	datar = pandas.read_sql('SELECT p.nationality, SUM(s.mins_played) AS mins_played FROM CurrentSeasonStats s left join Player p ON s.Player_pid = p.pid GROUP BY p.nationality', con)
	return render_template('index.html', table=datar)


@app.route('/players', methods=['GET', 'POST'])
def players():
	con = create_engine('mysql+pymysql://guest:guest@ix.cs.uoregon.edu:3640/fpl', echo=False)
	country = request.form['country']
	data = pandas.read_sql("SELECT name, nationality FROM Player WHERE nationality LIKE '" + country + "'", con)
	entries = data.T.to_dict().values()
	return render_template('players.html', entries=entries)


if __name__ == "__main__":
	random_port = random.randint(1000, 5000)  # In order to "ensure" no hosting overlaps
	app.run(host='128.223.4.35', port=random_port, debug=True)
