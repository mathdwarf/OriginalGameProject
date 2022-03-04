import os
import csv
from copy import deepcopy
import random

from character import Character

class Characters():
    CHARACTERS_PATH = os.path.abspath(os.path.join('./static/csv/characters.csv'))
    all = []
    
    @classmethod
    def get_all_characters(cls, csv_path=CHARACTERS_PATH):
        character_dict_info = []
        file = open(csv_path, 'r', encoding='utf8', errors='', newline='')
        dict_reader = csv.DictReader(file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        for dict_info in dict_reader:
            cls.all.append(Character(dict_info))
            
        return character_dict_info
    
    def __init__(self):
        if len(Characters.all) <= 0:
            self.get_all_characters()
    
    def summon_random(self, count=1):
        summoned = []
        characters = []
        if len(Characters.all) > count:
            characters = random.sample(Characters.all, count)
        else:
            characters = Characters.all
            
        for character in characters:
            character = deepcopy(character)
            summoned.append(character)
        
        return summoned

    def summon_specify(self, ids):
        summoned = []
        for id in ids:
            if type(id) != int:
                id = int(id)

            if len(Characters.all) > id:
                character = deepcopy(Characters.all[id])
                summoned.append(character)
        
        return summoned

    def show_all(self):
        for character in Characters.all:
            character.show_info()
    
    def show_characters(self, characters):
        for character in characters:
            character.show_info()
