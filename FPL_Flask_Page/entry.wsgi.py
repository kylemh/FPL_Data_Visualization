from flask import Flask, request, render_template
import pandas
from sqlalchemy import create_engine


app = Flask(__name__)



@app.route('/')
def index():
	con=create_engine('mysql+mysqldb://zoeo:Moraga17.@ix.cs.uoregon.edu:3640/sport', echo=False)
	#get data
	datar=pandas.read_sql('SELECT * FROM players', con)
	
	return render_template('index.html', table=datar)



@app.route('/players', methods = ['GET', 'POST'])
def players():
	con=create_engine('mysql+mysqldb://zoeo:Moraga17.@ix.cs.uoregon.edu:3640/sport', echo=False)
	country = request.form['country']
	data=pandas.read_sql("SELECT id, nationality FROM players WHERE nationality LIKE '" + country + "'", con)
	#cursor.execute("SELECT id, nationality FROM players WHERE nationality LIKE '" + country + "'")
	#entries = [dict(id=row[0], nationality=row[1]) for row in datar]
	entries = data.T.to_dict().values()
	return render_template('players.html', entries = entries)




if __name__ == "__main__":
	app.run(host='128.223.4.35', port=5558, debug=True)
