# Import dependencies
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

print(roster)