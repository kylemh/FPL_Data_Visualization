from flask import Flask, request, render_template
import pandas as pd
from sqlalchemy import create_engine


app = Flask(__name__)


@app.route('/')
def index():
    con = create_engine('mysql+pymysql://guest:guest@ix.cs.uoregon.edu:3640/fpl', echo=False)

    table_query = ("SELECT p.nationality, SUM(s.mins_pl) AS mins_pl FROM CurrentSeasonStats s "
                   "LEFT JOIN Player p ON s.Player_pid = p.pid GROUP BY p.nationality")
    datar = pd.read_sql(table_query, con)

    return render_template('index.html', table=datar)


@app.route('/players', methods=['GET', 'POST'])
def players():
    con = create_engine('mysql+pymysql://guest:guest@ix.cs.uoregon.edu:3640/fpl', echo=False)

    country = request.form['country']
    players_by_country = ("SELECT name, nationality FROM Player WHERE nationality LIKE %s", country)
    data = pd.read_sql(players_by_country, con)
    entries = data.T.to_dict().values()

    return render_template('players.html', entries=entries, user_input=country)


@app.route('/goals', methods=['GET', 'POST'])
def goals():
    con = create_engine('mysql+pymysql://guest:guest@ix.cs.uoregon.edu:3640/fpl', echo=False)

    goal = request.form['goal']
    players_by_goals = ("SELECT p.name, r.gameweek, s.goals_scored FROM Player p "
                        "LEFT JOIN PlayerResultStats s ON p.pid = s.Player_pid "
                        "LEFT JOIN Result r ON s.Result_id = r.id "
                        "WHERE s.goals_scored >= %s", goal)

    data = pd.read_sql(players_by_goals, con)
    entries = data.T.to_dict().values()

    return render_template('goals.html', entries=entries)


@app.route('/stats', methods=['GET', 'POST'])
def stats():
    con = create_engine('mysql+pymysql://guest:guest@ix.cs.uoregon.edu:3640/fpl', echo=False)

    stat = request.form['stat']
    players_by_stats = ("SELECT p.name, p.position, c.total_points, c.mins_played, "
                        "c.goals_scored, c.assists, c.clean_sheets, c.own_goals, "
                        "c.penalties_saved, c.penalties_missed, c.yellow_cards, c.red_cards, "
                        "c.saves, c.ea_index, c.influence, c.creativity, c.threat, c.ict_index "
                        "FROM Player p LEFT JOIN CurrentSeasonStats c ON p.pid = c.Player_pid "
                        "WHERE p.name LIKE %s", stat)
    data = pd.read_sql(players_by_stats, con)
    entries = data.T.to_dict().values()

    return render_template('stats.html', entries=entries)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
