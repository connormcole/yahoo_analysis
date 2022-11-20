# Import dependencies
import json
from typing import Union, List, Dict, Callable, Type, Any
from pathlib import Path, PosixPath

from yfpy import Data
from yfpy.models import Game, StatCategories, User, Scoreboard, Settings, Standings, League, Player, Team, \
    TeamPoints, TeamStandings, Roster
from yfpy.query import YahooFantasySportsQuery
#from yfpy.utils import complex_json_handler, unpack_data
from yahoo_oauth import OAuth2
import yahoo_fantasy_api as yfa

# Connect to yahoo api
sc = OAuth2(None, None, from_file='oauth2.json')

# Game object
gm = yfa.Game(sc, 'nfl')

# List of leagues tied to my account
leagues = gm.league_ids()

# Print full list of leagues tied to my account. Verify it matches my most recent league on yahoo fantasy site
print(leagues)

# League object with most recent season league id
lg = gm.to_league('414.l.63110')

# Get team key from the league
teamkey = lg.team_key()

# Get the team object
team = lg.to_team(teamkey)

# Get team roster
roster = team.roster()

# https://football.fantasysports.yahoo.com/f1/63110 = yahoo url location for linclon 
query = YahooFantasySportsQuery(auth_dir = "C:/Users/conno/Desktop/yahoo_analysis", league_id="414.l.63110", browser_callback=False)
team_stats = query.get_team_stats(1)
