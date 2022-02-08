import os
import csv
from numpy.random import randint

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
            
            self.summoned = []
    
    def summon_random(self, count=1):
        if len(Characters.all) > 0:
            for _ in range(count):
                character = Characters.all[randint(0, len(Characters.all))]
                self.summoned.append(character)

    def summon_specify(self, id):
        if type(id) != int:
            id = int(id)

        character = Characters.all[id]
        self.summoned.append(character)

    def show_all(self):
        for character in Characters.all:
            character.show_info()
    
    def show_summoned(self):
        for character in self.summoned:
            character.show_info()
