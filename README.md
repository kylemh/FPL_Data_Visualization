# Fantasy Premiere League Data Exploration

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Zoe Olson, Kyle Holmberg, and Ryan Collier set out a goal to learn about data collection, analyzation, and visualization.

We chose the English Premier League as our source of data, with an emphasis on improving [Fantasy Premier League](https://fantasy.premierleague.com) scores.


## Table of Contents

- [Resources Used](#resources-used)
- [Install](#install)
- [Contents](#contents)
- [Contribute](#contribute)
- [License](#license)


## Resources Used

https://www.cs.uoregon.edu/Classes/16F/cis451/final.html

[FPL Bootstrap API Endpoint](https://fantasy.premierleague.com/drf/bootstrap-static)

[FPL Player API Endpoints (1 to a variable number around 656)](https://fantasy.premierleague.com/drf/element-summary/1)

[Similar Project](https://llimllib.github.io/fantasypl/)

[Asynchronous HTTP Requests in Python 3.5+](http://scribu.net/blog/asynchronous-http-requests-in-python-3.5.html)

[Making 1 million requests with python-aiohttp](https://pawelmhm.github.io/asyncio/python/aiohttp/2016/04/22/asyncio-aiohttp.html)


## Install

Please install [Virtual Environments](https://pypi.python.org/pypi/virtualenv).


**Webscraper**

1. Clone repository.
2. Open terminal within repo/webscraper/
3. Create and activate your virtual environment.
4. `$ pip3 install -r requirements.txt`
5. `$ python3 fpl_csv_converter.py`


**Flask App**

1. Install [Homebrew](https://brew.sh/)
2. Open terminal and use `$ brew install mysql`
3. Clone repository.
4. Change directories in terminal to repo/
5. `$ mysql -u <username> -p <password> <database name> < create_fpl_models.sql`
6. `$ cd app`
6. (Temporary) Edit line 23 of entry.wsgi.py to local MySQL DB location.
7. Create and activate your virtual environment.
8. `$ pip3 install -r requirements.txt`
9. `$ python3 entry.wsgi.py`


## Contents

**To view our Jupyter Notebook, click [HERE](http://nbviewer.jupyter.org/github/kylemh/FPL_Data_Visualization/blob/master/jupyter_notebook/Jupyter_viz.ipynb)**

```
├── LICENSE
├── README.md
├── app
│   ├── entry.wsgi.py
│   ├── requirements.txt
│   ├── static
│   └── templates
├── create_fpl_model.sql
├── docs
│   ├── CIS407_Retrospective.pdf
│   ├── CIS451_Final_Report.pdf
│   ├── Retrospective.pdf
│   └── create_fpl_model.sql
├── jupyter_notebook
│   ├── Jupyter_viz.ipynb
│   ├── README.md
│   └── jupyter_viz_files
├── mysql_dump.sql
└── webscraper
    ├── CurrentSeasonStats.csv
    ├── History.csv
    ├── Managers.csv
    ├── Player.csv
    ├── PlayerResultStats.csv
    ├── Result.csv
    ├── Teams.csv
    ├── TotalPastStats.csv
    ├── fpl_csv_converter.py
    └── requirements.txt
```


## Contribute

#### What's Finished
* Statistical Analysis with Visuals: Jupyter Notebook utilizing pandas and matplotlib
* Data Collection: Python Web Scraper that converts API endpoint JSON into a MySQL Database
* Interactive Data Visualization(s): d3.js, matplotlib, pandas, and Flask

#### What's Left
* Webscraper Refactor
* Flask App Redesign (planned 2017-2018 season release)
* Create an automated Fantasy Manager


## License

[MIT](LICENSE) © Kyle Holmberg
