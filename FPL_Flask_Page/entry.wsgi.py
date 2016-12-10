from flask import Flask, request, render_template
import pandas
from sqlalchemy import create_engine


app = Flask(__name__)



@app.route('/')
def index():
	con=create_engine('mysql+mysqldb://zoeo:Moraga17.@ix.cs.uoregon.edu:3640/fpl', echo=False)
	#get data
	#datar=pandas.read_sql('SELECT nationality FROM Player', con)
	datar=pandas.read_sql('SELECT p.nationality, SUM(s.mins_played) AS mins_played FROM CurrentSeasonStats s left join Player p ON s.Player_pid = p.pid GROUP BY p.nationality', con)
	return render_template('index.html', table=datar)



@app.route('/players', methods = ['GET', 'POST'])
def players():
	con=create_engine('mysql+mysqldb://zoeo:Moraga17.@ix.cs.uoregon.edu:3640/fpl', echo=False)
	country = request.form['country']
	data=pandas.read_sql("SELECT name, nationality FROM Player WHERE nationality LIKE '" + country + "'", con)
	#cursor.execute("SELECT id, nationality FROM players WHERE nationality LIKE '" + country + "'")
	#entries = [dict(id=row[0], nationality=row[1]) for row in datar]
	entries = data.T.to_dict().values()
	return render_template('players.html', entries = entries)




if __name__ == "__main__":
	app.run(host='128.223.4.35', port=5558, debug=True)
