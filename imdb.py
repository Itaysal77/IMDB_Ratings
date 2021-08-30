import requests
import json
import Tkinter


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


if __name__ == "__main__":
    gui=Tkinter.Tk()

    name = raw_input("Enter Movie name \n")
        year=input("Enter Movie year if known, else enter 0 \n")

    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

    querystring = {"s": name, "page": "1", "r": "json"}

    headers = {
        'x-rapidapi-key': "9889bdf98emsha6a9d29002fc13cp17642ejsn27c857b6eaa4",
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
   all=response.json()["Search"]
    if year!="0":
        ind = next((index for (index, d) in enumerate(all) if d["Year"] == f'{year}'), None)
    else: ind=0
        
    id=all[ind]["imdbID"]
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

    querystring = {"i": id, "r": "json"}

    headers = {
        'x-rapidapi-key': "9889bdf98emsha6a9d29002fc13cp17642ejsn27c857b6eaa4",
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    rating = response.json()["imdbRating"]

    print (f'The rating of {name} that came out in {year} is:  {rating}')
