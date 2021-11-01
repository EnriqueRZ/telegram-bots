import requests

url = "https://baseball-data.p.rapidapi.com/match/list/results"

querystring = {"date":"09/10/2021"}

headers = {
    'x-rapidapi-host': "baseball-data.p.rapidapi.com",
    'x-rapidapi-key': "636275c1camsh9b6fec774628500p1e6071jsndb1b276935f3"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)