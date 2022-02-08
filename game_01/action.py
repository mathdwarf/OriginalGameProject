class Action():
    def __init__(self, dict_info):
        self.id = dict_info['id']
        self.name = dict_info['name']
        self.target = dict_info['target']
        self.effect_max = dict_info['effect_max']
        self.effect_min = dict_info['effect_min']
        self.hit_rate = dict_info['hit_rate']
        self.mp_cost = dict_info['mp_cost']

    def show_info(self):
        print(f'        {self.name}')
        print(f'            対象　　：{self.target}')
        print(f'            ダメージ：{self.effect_min}～{self.effect_max}')
        print(f'            命中率　：{self.hit_rate}')
        print(f'            消費MP　：{self.mp_cost}')