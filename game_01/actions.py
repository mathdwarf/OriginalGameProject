import os
import csv

from action import Action

class Actions():
    ACTIONS_PATH = os.path.abspath(os.path.join('./static/csv/actions.csv'))
    all = []
    
    @classmethod
    def get_all_actions(cls, csv_path=ACTIONS_PATH):
        action_dict_info = []
        file = open(csv_path, 'r', encoding='utf8', errors='', newline='')
        dict_reader = csv.DictReader(file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        for dict_info in dict_reader:
            cls.all.append(Action(dict_info))
            
        return action_dict_info
    
    def __init__(self):
        if len(Actions.all) <= 0:
            Actions.get_all_actions()
            
        self.list = []
    
    def construct(self, action_ids):
        for action_id in action_ids:
            id = int(action_id)
            if id < len(Actions.all):
                self.list.append(Actions.all[id])
 
    def show_info(self):
        print('    アクション：')
        for action in self.list:
            action.show_info()