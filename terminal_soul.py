import random

def generate_damage(min:int, max:int):
    return random.randint(min,max)


def show_state(name_h:str, hp_h:int, name_e:str, hp_e:int):
    print("\n    STATE    \n")
    print(name_h, "| Hp:", hp_h)
    print(name_e, "| Hp:", hp_e)
    print()


def player_turn(hp_h:int, hp_e:int,potions:int):
    
   
    op = input("Choose an option to take:\n" \
    "1. Attack\n" \
    "2. Heal\n" \
    "3. Special Ability\n" \
    "-> ").lower()

    if op == "attack" or op == "1":
        damage_hero = generate_damage(10, 25)
        hp_e -= damage_hero
        print("You have hit by:",damage_hero , "points of damage")

    elif op == "heal" or op == "2":
        
        if potions > 0:
            hp_h += 20
            potions -= 1
            print("You have been healed  by +20HP points of health")
        else:
            print("No potions left!")

    elif op == "special ability" or op == "3":

        probability = random.randint(0,1)
        if probability == 0:
            print("You have failed")
        else:
            damage_hero = generate_damage(30,50)
            hp_e -= damage_hero
            print("You have attacked by ", damage_hero, "points of damage")
       
    else:
        print("\nChoose the key word or a number") 

    return hp_h, hp_e, potions   


def enemy_turn (hp_h:int):
    enemy_damage = generate_damage(15, 20)
    hp_h -= enemy_damage
    print("Enemy has hit you by -", enemy_damage,"points of damage")

    return hp_h


def verify_winner(hp_h:int,hp_e:int):

    if hp_h <= 0:
        print("\nYou lost :(")
        return True
    
    elif hp_e <= 0:
        print("\nYou won! :)")
        return True

    else:
        return False


print("Street Fighter - Badass Version")
name_enemy =  "Ares" 
print("\nYour Enemy's name:", name_enemy)
name_hero = input("\nChoose your hero's name: ")

hp_hero = 100 # inicialized hero's hp 100 by default
hp_enemy = 120 # inicialized enemy's hp 120 by default.
potions = 3

game_over = False

while game_over == False:
    hp_hero,hp_enemy,potions = player_turn(hp_hero, hp_enemy, potions) # storing what function is giving
    game_over = verify_winner(hp_hero,hp_enemy)
    if game_over == False:
        hp_hero = enemy_turn(hp_hero)
        game_over = verify_winner(hp_hero,hp_enemy)
    
    show_state(name_hero,hp_hero,name_enemy,hp_enemy)



    

