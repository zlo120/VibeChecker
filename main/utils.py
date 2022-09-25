import requests
import random
def generateDesc(name, isVibe):
    adj1 = ["sharing", "kind", "caring", "curious"]
    adj2 = ["insightful", "intelligent", "funny", "outgoing"]
    adj3 = ["adventurous", "charismatic", "spontaneous"]
    adj4 = ["discreet", "open", "honest", "courageous"]
    adj5 = ["captivating", "studious", "self-awareness", "wholeheartedness"]
    
    adjj1 = ["pedantic", "selfishness", "pessimistic", "jealousy"]
    adjj2 = ["insulting", "impulsiveness", "crudness", "resentfulness"]
    adjj3 = ["disorderly", "grumpy", "annoying", "bossy"]
    adjj4 = ["argumentative", "smarty-pants", "teachers pet", "lazy"]
    adjj5 = ["thievish", "know-it-all", "rude", "disobedient"]
    if isVibe:
        return f"A lot can be assumed when you first see {name}, but the two traits most people enjoy the most are that he's {adj1[random.randint(0, len(adj1)-1)]} and {adj2[random.randint(0, len(adj2)-1)]}. Of course he's also {adj3[random.randint(0, len(adj3)-1)]}, {adj4[random.randint(0, len(adj4)-1)]} and {adj5[random.randint(0, len(adj5)-1)]}. His {adj1[random.randint(0, len(adj1)-1)]} nature though, this is what he's pretty much loved for. People often count on this and his {adj2[random.randint(0, len(adj2)-1)]} nature whenever they need cheering up."
    else:
        return f"Many hateful words can be said about {name}, but the fact he's {adjj1[random.randint(0, len(adjj1)-1)]} and {adjj2[random.randint(0, len(adjj2)-1)]} is just the tip of the iceberg. On top of that he's also {adjj3[random.randint(0, len(adjj3)-1)]}, {adjj4[random.randint(0, len(adjj4)-1)]} and {adjj5[random.randint(0, len(adjj5)-1)]}, but they're not as prominent and counteracted by habits of being perceptive as well. There's a great deal of pain left on all sides because of this and his grim ways, which is far from desired, but so be it."

def getGi2f(query):
    request = f"https://tenor.googleapis.com/v2/search?q={query}&key=AIzaSyB8jjGOU96tvKOl6SEa6ZftomW9P9sp5Wc&client_key=Vibe_Checker&limit=1"
    response = requests.get(request)
    if response.status_code == 200:
        print("sucessfully fetched the data")
        response = response.json()
        first_res = response['results'][0]["media_formats"]["gif"]["url"]
        return first_res
    else:
        print(f"Hello person, there's a {response.status_code} error with your request")

def getGif(query):
    request = f"https://tenor.googleapis.com/v2/search?q={query}&key=AIzaSyB8jjGOU96tvKOl6SEa6ZftomW9P9sp5Wc&client_key=Vibe_Checker&limit=11"
    response = requests.get(request)
    if response.status_code == 200:
        print("sucessfully fetched the data")
        response = response.json()
        first_res = response['results'][random.randint(0,10)]["media_formats"]["gif"]["url"]
        return first_res
    else:
        print(f"Hello person, there's a {response.status_code} error with your request")