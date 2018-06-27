# Python wrapper for Sportradar APIs
[![Build Status](https://travis-ci.org/johnwmillr/SportradarAPI.svg?branch=master)](https://travis-ci.org/johnwmillr/SportradarAPI)
[![PyPI version](https://badge.fury.io/py/sportradar.svg)](https://pypi.org/project/sportradar/)
[![Python version](https://img.shields.io/badge/python-3.x-brightgreen.svg)](https://pypi.org/project/sportradar/)

This is a Python wrapper for the sports APIs provided by [Sportradar](https://developer.sportradar.com/io-docs). You'll need to [sign up](https://developer.sportradar.com/member/register) for an API key to use the service. Luckily, Sportradar provides a free tier that allows for 1,000 API queries per month and up to 1 query per second. The package currently only supports the [Soccer INTL Trial v3](https://developer.sportradar.com/files/indexSoccer.html) API, but I hope to expand it to support their APIs for other sports in the future.

## Supported APIs
| Sport         | Wrapper       | Tests  |
|:-------------|:-------------:|:-----:|
| [Soccer](https://developer.sportradar.com/docs/read/Soccer_API)  :soccer: | :heavy_check_mark: | :heavy_check_mark: |
| [Darts](https://developer.sportradar.com/files/indexDarts.html)   :dart:   | :heavy_check_mark: |   |
| [Beach volleyball](https://developer.sportradar.com/files/indexVolleyball.html) :palm_tree: | :heavy_check_mark: |   |

## Installation
The easiest way to start using this package is to install it via [PyPI](https://pypi.org/project/sportradar/) using `pip`:

`$pip install sportradar`

If you'd prefer to clone the repository and install it yourself, follow these steps:
1. Clone this repo:
`$git clone https://github.com/johnwmillr/SportradarAPI.git`
2. Enter the cloned directory:
`$cd SportradarAPI`
3. Install:
`$python setup.py install`

## Usage
Below is a brief demonstration of using the package to download data for the 2018 FIFA World Cup.

```python
from sportradar import Soccer

# Create an instance of the Sportradar Soccer API class
sr = Soccer.Soccer("paste your api key here")

# Get a list of all tournaments
tournaments = sr.get_tournaments().json()

# Get info on the 2018 World Cup (Teams, Rounds, etc.)
worldcup = sr.get_tournament_info(tournaments['tournaments'][4]['id']).json()

# Get more information on each team in the World Cup
teams = []
team_counter = 0
for group in worldcup['groups']:
    for team in group['teams']:
        team_counter += 1
        team_id = team['id']
        team_name = team['name']
        print("({}): {}, {}".format(team_counter, team_name, team_id))
        try:
            teams.append(sportsradar.get_team_profile(team_id).json())
        except Exception as e:
            print("Error: {}".format(e))
        time.sleep(5) # wait 5 seconds before next API call

# Save the team data to a .json file
print("Saving the data...", end="", flush=True)
with open("world_cup_team_data.json", "w") as outfile:
    json.dump(teams, outfile)
print(" Done.")

```

## Example projects
  - [2018 FIFA World Cup player stats](https://www.johnwmillr.com/fifa-world-cup-data/)
