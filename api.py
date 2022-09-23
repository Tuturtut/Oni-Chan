import requests

from config import apiToken
titre = "Black Summoner"
print(titre)

response = requests.get("https://api.themoviedb.org/3/search/tv?api_key=" + apiToken + "&language=fr-FR&page=1&query=" + titre + "&include_adult=true")

id = response.json()["results"][0]["id"]


oniStreamResponse = requests.get("https://oni-stream.com/api/listanimes/" + str(id))


if oniStreamResponse.status_code == 404:
    print("L'anime n'existe pas sur oni-stream")
else:
    print(oniStreamResponse.json()["url"])