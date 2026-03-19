import random

def generate_damage(min:int, max:int):
    return random.randint(min,max)

def show_state(name_h:str,hp_h:int,name_e:str,hp_e:int):
    life_max  = 100
    visual_bar = 10

    porcentage_h = hp_h/life_max
     

hero_hp = 100
enemy_hp = 120
potion = 3

# while hero_hp <= 0 or enemy_hp <= 0:

#     if potion == 3:
#         potion -= 1
