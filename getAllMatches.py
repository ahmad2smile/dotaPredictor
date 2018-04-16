import requests
import json

res = requests.get(
    "https://api.opendota.com/api/players/103296833/matches")
with open("matches.json", "w") as matchesFile:
    json.dump(res.json(), matchesFile)

matchesFile.close()
