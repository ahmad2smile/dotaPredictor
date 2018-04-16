import requests
import json

res = requests.get("https://api.opendota.com/api/heroes")

with open("heros.json", "w") as herosFile:
    json.dump(res.json(), herosFile)

herosFile.close()
