import random

def generate_damage(min:int, max:int):
    return random.randint(min,max)

def show_state(name_h:str, hp_h:int, name_e:str, hp_e:int):

    visual_bar_h = 10

    remaining_life_h = hp_h // visual_bar_h
    remaing_demage_h = visual_bar_h - (hp_h // visual_bar_h)

    print("Name:", name_h, "[" + "#" * remaining_life_h + "-" * remaing_demage_h + "]" )

    visual_bar_e = 12

    remaining_life_e = hp_e // visual_bar_e
    remaing_demage_e = visual_bar_e - (hp_e // visual_bar_e)

    print("Name:", name_e, "[" + "#" * remaining_life_e + "-" * remaing_demage_e + "]" )

def player_turn(hp_hero):
    
    potion = 3
    op = input("Choose an option to take:\n" \
    "1. Attack\n" \
    "2. Heal\n" \
    "3. Special Ability\n" \
    "-> ").lower()

    if op == "attack" or op == "1":

        print("You have hit by:", generate_damage(10, 25), "point of damages")

    elif op == "heal" or op == "2":
        
        if potion == 3:
            potion -= 1
            hp_hero += 20
            print("You have 2 potions left and have been healed by +20 Hp")
        elif potion == 2:
            potion -= 1
            hp_hero += 20
            print("You have 1 potions left and have been healed by +20 Hp")
        elif potion == 1:
            potion -= 1
            hp_hero += 20
            print("You just used all potions and have been healed by +20 Hp")
        else:
            print("What are you doing? No potions!")


    elif op == "special ability" or op == "3":

        probability = random.randint(0,1)
        if probability == 0:
            print("You have failed")
        else:
            print("You have attacked by ", generate_damage(30,50), "point of damages")
  

        print("You have been healed  by", hp_hero,"points of health")
    
    else:
        print("\nChoose the key word or a number")
    
    
    

def enemy_turn (hp_h):
    enemy_damage = generate_damage(15, 20)
    hp_h -= enemy_damage
    print("Enemy has hit you by -", enemy_damage,"points of damage")
    

def verify_winner(hp_h:int,hp_e:int):
    if hp_h == 0 or hp_e == 0:
        return True

name_hero = input("Choose your hero's name: ") # inicialized with input
name_enemy =  "Ares" # inicialized so it uses later on input
hp_hero = 100 # inicialized hero's hp 100 by default
hp_enemy = 120 # inicialized enemy's hp 120 by default.
game_over = False
while game_over != True:
    
    player_turn(hp_hero)

    enemy_turn(hp_hero)

    show_state(name_hero, hp_hero, name_enemy, hp_enemy)

    verify_winner(hp_hero, hp_enemy)
    

