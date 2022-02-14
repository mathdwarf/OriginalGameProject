from numpy.random import randint
from common import print_message
from characters import Characters

class Coliseum():
    ALLY  = 0
    ENEMY = 1
    
    characters = Characters()

    def __init__(self):
        self.allies = []
        self.enemies = []
    
    def make_battler_list(self):
        all = []
        all.extend(self.allies)
        all.extend(self.enemies)
        
        return all

    def call_allies(self, count=1):
        allies = Coliseum.characters.summon_random(count)
        [self.allies.append((ally, Coliseum.ALLY)) for ally in allies]
    
    def call_enemies(self, count=1):
        enemies = Coliseum.characters.summon_random(count)
        [self.enemies.append((enemy, Coliseum.ENEMY)) for enemy in enemies]
    
    def set_action_order(self):
        battler_list = []
        for ally in self.allies:
            battler_list.append(ally)
        for enemy in self.enemies:
            battler_list.append(enemy)
        
        battler_list =  sorted(battler_list, reverse=True, key=lambda battler: battler[0].speed)
        return battler_list
    
    def select_target(self, target, is_in_allies):
        target_battler_list = []
        if target == 'one':
            all = self.make_battler_list()
            target_battler = all[randint(0, len(all))] if (len(all) > 0) else None
            target_battler_list.append(target_battler) if target_battler != None else None
        
        elif target == 'all':
            all = self.make_battler_list()
            [target_battler_list.append(one) for one in all]
        
        elif target == 'ally':
            target_battler = \
                (self.allies[randint(0, len(self.allies))] if (len(self.allies) > 0) else None) if is_in_allies else \
                (self.enemies[randint(0, len(self.enemies))] if (len(self.enemies) > 0) else None)
            target_battler_list.append(target_battler) if target_battler != None else None
        
        elif target == 'allies':
            [target_battler_list.append(ally) for ally in self.allies] if is_in_allies else \
            [target_battler_list.append(enemy) for enemy in self.enemies]
        
        elif target == 'enemy':
            target_battler = \
                (self.enemies[randint(0, len(self.enemies))] if (len(self.enemies) > 0) else None) if is_in_allies else \
                (self.allies[randint(0, len(self.allies))] if (len(self.allies) > 0) else None)
            target_battler_list.append(target_battler) if target_battler != None else None
        
        elif target == 'enemies':
            [target_battler_list.append(enemy) for enemy in self.enemies] if is_in_allies else \
            [target_battler_list.append(ally) for ally in self.allies]
        
        else:
            pass # Do Nothing
        
        return target_battler_list
    
    def calculate_damage_point(self, max, min, hit_rate):
        damage_point = 0
        is_hit = True if (randint(1, 100) < hit_rate) else False
        if is_hit:
            damage_point = randint(min, max+1)
        else:
            print_message('　ミス ！')
        
        return damage_point
    
    def execute_action(self, battler):
        if battler[0].cur_hp <= 0:
            print(f'　{battler[0].name} は せんとうふのう だ ！')
            return
        else:
            action = battler[0].select_action()
            if battler[0].cur_mp < action.mp_cost:
                print_message('　MP が たりない ！')
                return
            
            print_message(f'　{battler[0].name} の {action.name} ！', end='')
            battler[0].cur_mp -= action.mp_cost
            is_battler_in_allies = True if battler[1] == Coliseum.ALLY else False
            target_list = self.select_target(action.target, is_battler_in_allies)
            for target in target_list:
                damage_point = self.calculate_damage_point(action.effect_max, action.effect_min, action.hit_rate)
                
                print_message('　みかた の ', end='') if target[1] == Coliseum.ALLY else print_message('　てき の', end='')
                print_message(f'{target[0].name} に ', end='')
                print_message(f'{str(damage_point)} の ダメージ ！') if damage_point >= 0 else print_message(f'{str(damage_point * -1)} の かいふく ！')
                
                if target[0].cur_hp < damage_point:
                    target[0].cur_hp = 0
                    print_message(f'{target[0].name} は せんとうふのう に なった ！')
                else:
                    if target[0].cur_hp <= 0:
                        print_message(f'{target[0].name} は せんとうふのう のため かいふく できない ！')
                    else:
                        if target[0].max_hp > (target[0].cur_hp-damage_point):
                            target[0].cur_hp -= damage_point
                        else:
                            target[0].cur_hp = target[0].max_hp
    
    def show_battlers_status(self):
        print_message(f'みかた の じょうたい')
        for ally in self.allies:
            ally_name = f'　{ally[0].name}'
            ally_hp = f'HP : {str(ally[0].cur_hp)} / {str(ally[0].max_hp)}'
            ally_mp = f'MP : {str(ally[0].cur_mp)} / {str(ally[0].max_mp)}'
            print_message(f'{ally_name} : {ally_hp}, {ally_mp}')
        print_message(f'てき の じょうたい')
        for enemy in self.enemies:
            enemy_name = f'　{enemy[0].name}'
            enemy_hp = f'HP : {str(enemy[0].cur_hp)} / {str(enemy[0].max_hp)}'
            enemy_mp = f'MP : {str(enemy[0].cur_mp)} / {str(enemy[0].max_mp)}'
            print_message(f'{enemy_name} : {enemy_hp}, {enemy_mp}')
    
    def check_settlement(self):
        result = 'yet'
        
        num_survive_allies = [s_allies for s_allies in self.allies if s_allies[0].cur_hp > 0]
        num_survive_enemies = [s_enemies for s_enemies in self.enemies if s_enemies[0].cur_hp > 0]
        if (len(num_survive_allies) <= 0) & (len(num_survive_enemies) <= 0):
            result = 'draw'
        elif len(num_survive_allies) <= 0:
            result = 'lose'
        elif len(num_survive_enemies) <= 0:
            result = 'win'
        else:
            result = 'yet'
        
        return result
    
    def execute_turn(self):
        battlers_order = self.set_action_order()
        for battler in battlers_order:
            print_message('みかた の ', end='') if battler[1] == Coliseum.ALLY else print_message('てき の', end='')
            print_message(f'{battler[0].name} の ターン ！')
            self.execute_action(battler)
        
        self.show_battlers_status()
    
    def execute_battle(self):
        self.call_allies(3)
        self.call_enemies(3)
        
        settlement = self.check_settlement()
        while settlement == 'yet':
            self.execute_turn()
            print_message('エンター を おして たたかい を つづける ( ちゅうし は q を おして エンター)', end='')
            got_key = input('')
            if 'q' in got_key:
                settlement = 'quit'
            else:
                settlement = self.check_settlement()
        
        if settlement == 'win':
            print_message('たたかい に しょうり した ！')
        elif settlement == 'lose':
            print_message('たたかい に まけて しまった ！')
        elif settlement == 'draw':
            print_message('たたかい は ひきわけ に おわった ！')
        elif settlement == 'quit':
            print_message('たたかい は ちゅうし に なった ！')
        else:
            print_message('ひじょう じたい が はっせい した ！')

if __name__ == '__main__':
    print_message('せんとう かいし ！')
    coliseum = Coliseum()
    coliseum.execute_battle()
