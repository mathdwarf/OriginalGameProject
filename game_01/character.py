from numpy.random import randint

from actions import Actions

class Character():
    def __init__(self, dict_info):
        self.name = dict_info['name']
        self.hp = dict_info['hp']
        self.mp = dict_info['mp']
        self.offense = dict_info['offense']
        self.defense = dict_info['defense']
        self.speed = dict_info['speed']
        self.wise = dict_info['wise']
        
        action_ids = dict_info['actions'].split(':')
        self.actions = Actions()
        self.actions.construct(action_ids)

    def decide_action(self):
        action = None
        if len(self.actions.list) > 0:
            action = self.actions.list[randint(0, len(self.actions.list))]
            
        return action

    def show_info(self):
        print(f'{self.name}')
        print(f'    HP　　　　：{self.hp}')
        print(f'    MP　　　　：{self.mp}')
        print(f'    攻撃力　　：{self.offense}')
        print(f'    防御力　　：{self.defense}')
        print(f'    素早さ　　：{self.speed}')
        print(f'    賢さ　　　：{self.wise}')
        self.actions.show_info()
