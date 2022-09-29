import requests
import random
from .type import *
from .models import Cards

def generateDesc(name, isVibe):
    adj1 = ["sharing", "kind", "caring", "curious"]
    adj2 = ["insightful", "intelligent", "funny", "outgoing"]
    adj3 = ["adventurous", "charismatic", "spontaneous"]
    adj4 = ["discreet", "open", "honest", "courageous"]
    adj5 = ["captivating", "studious", "self-awareness", "wholeheartedness"]
    
    adjj1 = ["pedantic", "selfishness", "pessimistic", "jealous"]
    adjj2 = ["insulting", "impulsiveness", "crudness", "resentfulness"]
    adjj3 = ["disorderly", "grumpy", "annoying", "bossy"]
    adjj4 = ["argumentative", "smarty-pants", "teachers pet", "lazy"]
    adjj5 = ["thievish", "know-it-all", "rude", "disobedient"]
    if isVibe:
        return f"A lot can be assumed when you first see {name}, but the two traits most people enjoy the most are that they are {adj1[random.randint(0, len(adj1)-1)]} and {adj2[random.randint(0, len(adj2)-1)]}. Of course they are also {adj3[random.randint(0, len(adj3)-1)]}, {adj4[random.randint(0, len(adj4)-1)]} and {adj5[random.randint(0, len(adj5)-1)]}. Their {adj1[random.randint(0, len(adj1)-1)]} nature though, this is what they're pretty much loved for. People often count on this and their {adj2[random.randint(0, len(adj2)-1)]} nature whenever they need cheering up."
    else:
        return f"Many hateful words can be said about {name}, but the fact they're {adjj1[random.randint(0, len(adjj1)-1)]} and {adjj2[random.randint(0, len(adjj2)-1)]} is just the tip of the iceberg. On top of that they're also {adjj3[random.randint(0, len(adjj3)-1)]}, {adjj4[random.randint(0, len(adjj4)-1)]} and {adjj5[random.randint(0, len(adjj5)-1)]}, but they're not as prominent and counteracted by habits of being perceptive as well. There's a great deal of pain left on all sides because of this and their grim ways, which is far from desired, but so be it."

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

def createCharacter(name):

    ID = random.randint(1,10)

    person = None

    if ID == 1:
        gif = getGif(name)
        ck = CryptoKing(name)
        vibe = random.randint(0,1)
        description = str()
        if vibe:
            description = generateDesc(name, vibe)
        else:
            description = generateDesc(name, vibe)

        person = Cards(
            ImageURL = gif,
            Type = 1,
            Name = name,
            Strength = ck.strength,
            Intelligence = ck.intelligence,
            Wealth = ck.wealth,
            Laziness = ck.laziness,
            Clumsiness = ck.clumsiness,
            Description = description,
            isAVibe = vibe,
            URLCode = ck.URL
        )

    if ID == 2:
        gif = getGif(name)
        ff = FreedomFighter(name)
        vibe = random.randint(0,1)
        description = str()
        if vibe:
            description = generateDesc(name, vibe)
        else:
            description = generateDesc(name, vibe)

        person = Cards(
            ImageURL = gif,
            Type = 2,
            Name = name,
            Strength = ff.strength,
            Intelligence = ff.intelligence,
            Wealth = ff.wealth,
            Laziness = ff.laziness,
            Clumsiness = ff.clumsiness,
            Description = description,
            isAVibe = vibe,
            URLCode = ff.URL
        )

    if ID == 3:
        gif = getGif(name)
        sjw = SJW(name)
        vibe = random.randint(0,1)
        description = str()
        if vibe:
            description = generateDesc(name, vibe)
        else:
            description = generateDesc(name, vibe)

        person = Cards(
            ImageURL = gif,
            Type = 3,
            Name = name,
            Strength = sjw.strength,
            Intelligence = sjw.intelligence,
            Wealth = sjw.wealth,
            Laziness = sjw.laziness,
            Clumsiness = sjw.clumsiness,
            Description = description,
            isAVibe = vibe,
            URLCode = sjw.URL
        )

    if ID == 4:
        gif = getGif(name)
        CC = CertifiedChad(name)
        vibe = random.randint(0,1)
        description = str()
        if vibe:
            description = generateDesc(name, vibe)
        else:
            description = generateDesc(name, vibe)

        person = Cards(
            ImageURL = gif,
            Name = name,
            Type = 4,
            Strength = CC.strength,
            Intelligence = CC.intelligence,
            Wealth = CC.wealth,
            Laziness = CC.laziness,
            Clumsiness = CC.clumsiness,
            Description = description,
            isAVibe = vibe,
            URLCode = CC.URL
        )

    if ID == 5:
        gif = getGif(name)
        GJ = GymJunkie(name)
        vibe = random.randint(0,1)
        description = str()
        if vibe:
            description = generateDesc(name, vibe)
        else:
            description = generateDesc(name, vibe)

        person = Cards(
            ImageURL = gif,
            Name = name,
            Type = 5,
            Strength = GJ.strength,
            Intelligence = GJ.intelligence,
            Wealth = GJ.wealth,
            Laziness = GJ.laziness,
            Clumsiness = GJ.clumsiness,
            Description = description,
            isAVibe = vibe,
            URLCode = GJ.URL
        )

    if ID == 6:
        gif = getGif(name)
        TT = TiktokTart(name)
        vibe = random.randint(0,1)
        description = str()
        if vibe:
            description = generateDesc(name, vibe)
        else:
            description = generateDesc(name, vibe)

        person = Cards(
            ImageURL = gif,
            Name = name,
            Type = 6,
            Strength = TT.strength,
            Intelligence = TT.intelligence,
            Wealth = TT.wealth,
            Laziness = TT.laziness,
            Clumsiness = TT.clumsiness,
            Description = description,
            isAVibe = vibe,
            URLCode = TT.URL
        )

    if ID == 7:
        gif = getGif(name)
        NN = NetflixNinja(name)
        vibe = random.randint(0,1)
        description = str()
        if vibe:
            description = generateDesc(name, vibe)
        else:
            description = generateDesc(name, vibe)

        person = Cards(
            ImageURL = gif,
            Name = name,
            Type = 7,
            Strength = NN.strength,
            Intelligence = NN.intelligence,
            Wealth = NN.wealth,
            Laziness = NN.laziness,
            Clumsiness = NN.clumsiness,
            Description = description,
            isAVibe = vibe,
            URLCode = NN.URL
        )
        
    if ID == 8:
        gif = getGif(name)
        SI = SociallyInadequate(name)
        vibe = random.randint(0,1)
        description = str()
        if vibe:
            description = generateDesc(name, vibe)
        else:
            description = generateDesc(name, vibe)

        person = Cards(
            ImageURL = gif,
            Name = name,
            Type = 8,
            Strength = SI.strength,
            Intelligence = SI.intelligence,
            Wealth = SI.wealth,
            Laziness = SI.laziness,
            Clumsiness = SI.clumsiness,
            Description = description,
            isAVibe = vibe,
            URLCode = SI.URL
        )

    if ID == 9:
        gif = getGif(name)
        K = Karen(name)
        vibe = random.randint(0,1)
        description = str()
        if vibe:
            description = generateDesc(name, vibe)
        else:
            description = generateDesc(name, vibe)

        person = Cards(
            ImageURL = gif,
            Name = name,
            Type = 9,
            Strength = K.strength,
            Intelligence = K.intelligence,
            Wealth = K.wealth,
            Laziness = K.laziness,
            Clumsiness = K.clumsiness,
            Description = description,
            isAVibe = vibe,
            URLCode = K.URL
        )

    if ID == 10:
        gif = getGif(name)
        DelD = DelusionalDonut(name)
        vibe = random.randint(0,1)
        description = str()
        if vibe:
            description = generateDesc(name, vibe)
        else:
            description = generateDesc(name, vibe)

        person = Cards(
            ImageURL = gif,
            Name = name,
            Type = 10,
            Strength = DelD.strength,
            Intelligence = DelD.intelligence,
            Wealth = DelD.wealth,
            Laziness = DelD.laziness,
            Clumsiness = DelD.clumsiness,
            Description = description,
            isAVibe = vibe,
            URLCode = DelD.URL
        )

    if person != None:
        print(f"Creating person named {person.Name} of type {person.Type}")
        return person
    else: 
        return "Something went wrong with creating a person..."