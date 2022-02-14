from numpy.random import randint

from actions import Actions

class Character():
    def __init__(self, dict_info):
        self.name = dict_info['name']
        self.max_hp = dict_info['hp']
        self.cur_hp = self.max_hp
        self.min_hp = 0
        self.max_mp = dict_info['mp']
        self.cur_mp = self.max_mp
        self.min_mp = 0
        self.offense = dict_info['offense']
        self.defense = dict_info['defense']
        self.speed = dict_info['speed']
        self.wise = dict_info['wise']
        
        action_ids = dict_info['actions'].split(':')
        self.actions = Actions()
        self.actions.construct(action_ids)

    def select_action(self):
        action = self.actions.list[randint(0, len(self.actions.list))] if(len(self.actions.list) > 0) else None
        return action

    def show_info(self):
        print(f'{self.name}')
        print(f'    HP　　　　：{self.max_hp}')
        print(f'    MP　　　　：{self.max_mp}')
        print(f'    攻撃力　　：{self.offense}')
        print(f'    防御力　　：{self.defense}')
        print(f'    素早さ　　：{self.speed}')
        print(f'    賢さ　　　：{self.wise}')
        self.actions.show_info()
