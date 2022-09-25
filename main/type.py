from random import randint
from random import choice
from string import ascii_letters
from . import db
from flask import url_for

class CryptoKing:
    def __init__(self, name):
        self.name = name
        self.strength = randint(2,6)
        self.intelligence = randint(0,10)
        self.wealth = randint(0,10)
        self.laziness = randint(4,8)
        self.clumsiness = randint(0,10)
        self.URL = ID = '5' + ''.join(choice(ascii_letters) for i in range(6))
        
class FreedomFighter:
    def __init__(self, name):
        self.name = name
        self.strength = randint(6,10)
        self.intelligence = randint(3,10)
        self.wealth = randint(2,6)
        self.laziness = randint(0,3)
        self.clumsiness = randint(0,4)
        self.URL = ID = '5' + ''.join(choice(ascii_letters) for i in range(6))

class SJW:
    def __init__(self, name):
        self.name = name
        self.strength = randint(4,6)
        self.intelligence = randint(3,10)
        self.wealth = randint(2,6)
        self.laziness = randint(0,6)
        self.clumsiness = randint(3,10)
        self.URL = ID = '5' + ''.join(choice(ascii_letters) for i in range(6))

class CertifiedChad:
    def __init__(self, name):
        self.name = name
        self.strength = randint(4,8)
        self.intelligence = randint(3,10)
        self.wealth = randint(0,10)
        self.laziness = randint(0,6)
        self.clumsiness = randint(2,10)
        self.URL = ID = '5' + ''.join(choice(ascii_letters) for i in range(6))

class GymJunkie:
    def __init__(self, name):
        self.name = name
        self.strength = randint(8,10)
        self.intelligence = randint(3,7)
        self.wealth = randint(0,10)
        self.laziness = randint(0,4)
        self.clumsiness = randint(0,5)
        self.URL = ID = '5' + ''.join(choice(ascii_letters) for i in range(6))

class TiktokTart:
    def __init__(self, name):
        self.name = name
        self.strength = randint(0,6)
        self.intelligence = randint(3,6)
        self.wealth = randint(0,6)
        self.laziness = randint(5,10)
        self.clumsiness = randint(3,10)
        self.URL = ID = '5' + ''.join(choice(ascii_letters) for i in range(6))

class NetflixNinja:
    def __init__(self, name):
        self.name = name
        self.strength = randint(0,6)
        self.intelligence = randint(3,7)
        self.wealth = randint(0,6)
        self.laziness = randint(5,10)
        self.clumsiness = randint(3,10)
        self.URL = ID = '5' + ''.join(choice(ascii_letters) for i in range(6)) 

class SociallyInadequate:
    def __init__(self, name):
        self.name = name
        self.strength = randint(8,10)
        self.intelligence = randint(3,7)
        self.wealth = randint(0,6)
        self.laziness = randint(5,10)
        self.clumsiness = randint(6,10)
        self.URL = ID = '5' + ''.join(choice(ascii_letters) for i in range(6))

class Karen:
    def __init__(self, name):
        self.name = name
        self.strength = randint(4,6)
        self.intelligence = randint(0,3)
        self.wealth = randint(4,10)
        self.laziness = randint(0,10)
        self.clumsiness = randint(0,10)
        self.URL = ID = '5' + ''.join(choice(ascii_letters) for i in range(6))

class DelusionalDonut:
    def __init__(self, name):
        self.name = name
        self.strength = randint(0,8)
        self.intelligence = randint(3,5)
        self.wealth = randint(0,8)
        self.laziness = randint(5,10)
        self.clumsiness = randint(5,10)
        self.URL = ID = '5' + ''.join(choice(ascii_letters) for i in range(6))