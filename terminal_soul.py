import random

def generate_damage(min:int, max:int):
    return random.randint(min,max)

def show_state(name_h:str, hp_h:int, name_e:str, hp_e:int):
    # life_max  = 100
    visual_bar_h = 10

    remaining_life_h = hp_h // visual_bar_h
    remaing_demage_h = visual_bar_h - (hp_h // visual_bar_h)

    print("Name:", name_h, "[" + "#" * remaining_life_h + "-" * remaing_demage_h + "]" )

    visual_bar_e = 12

    remaining_life_e = hp_e // visual_bar_e
    remaing_demage_e = visual_bar_e - (hp_e // visual_bar_e)

    print("Name:", name_e, "[" + "#" * remaining_life_e + "-" * remaing_demage_e + "]" )

def player_turn():
    op = input("Choose an option to take:\n" \
    "1. Attack\n" \
    "2. Heal\n" \
    "3. Special Ability\n" \
    "-> ").lower()
    hp_h = 0
    if op == "attack" or op == "1":
        damage = generate_damage(10, 25)
        print("You have hit by:", damage, "point of damages")
    elif op == "heal" or op == "2":
        hp_h += 20
        print("You have been healed  by", hp_h,"points of health")
    elif op == "special ability" or op == "3":
        generate_damage(30, 50)


hero_hp = 100
enemy_hp = 120
potion = 3

# while hero_hp <= 0 or enemy_hp <= 0:

#     if potion == 3:
#         potion -= 1
