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

    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

    querystring = {"s": name, "page": "1", "r": "json"}

    headers = {
        'x-rapidapi-key': "9889bdf98emsha6a9d29002fc13cp17642ejsn27c857b6eaa4",
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    id=response.json()["Search"][0]["imdbID"]

    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

    querystring = {"i": id, "r": "json"}

    headers = {
        'x-rapidapi-key': "9889bdf98emsha6a9d29002fc13cp17642ejsn27c857b6eaa4",
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    rating = response.json()["imdbRating"]

    print ("The rating of " + name + " is: " + rating)
