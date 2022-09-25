import requests

def getGif(query):
    request = f"https://tenor.googleapis.com/v2/search?q={query}&key=AIzaSyB8jjGOU96tvKOl6SEa6ZftomW9P9sp5Wc&client_key=Vibe_Checker&limit=1"
    response = requests.get(request)
    if response.status_code == 200:
        print("sucessfully fetched the data")
        response = response.json()
        first_res = response['results'][0]["media_formats"]["gif"]["url"]
        return first_res
    else:
        print(f"Hello person, there's a {response.status_code} error with your request")