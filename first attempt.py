import random, time

hero_attack = 70
hero_parry = 40
hero_health = 10
enemy_attack = 70
enemy_parry = 40
enemy_health = 10
att_stance = 10 #increase att chance by 10% #reduce parry by 10%
def_stance = 10 #increase parry chance by 10% #reduce att by 10%
reckless_stance = 2

#loop should start before hit chances are rolled

while True :
    mod_hero_attack = hero_attack  #these "mod" variables are so that the att/def rates are reset at the begging of each round to the default values
    mod_hero_parry = hero_parry
    #mod_hero_health = 10
    mod_enemy_attack = enemy_attack
    mod_enemy_parry = enemy_parry
    #mod_enemy_health = 10

    
    
    action = input("Press 1 to Normal Attack or 2 for Aggresive Attack or 3 for Defensive Stance: ")
    print(".")
    print("You chose", action)
    print(".")
    action = int(action)
    
    if action == 2 : #FXIED problem here is that the att/def bonus stacks each round
        mod_hero_attack = mod_hero_attack + att_stance
        mod_hero_parry = mod_hero_parry - att_stance
        print("Hit Chance: ", str(mod_hero_attack) , "  ----  " , "Parry Chance: " , str(mod_hero_parry))
        
    if action == 3 :
        mod_hero_attack = mod_hero_attack - def_stance
        mod_hero_parry = mod_hero_parry + def_stance
        print("Hit Chance: ", str(mod_hero_attack) , "  ----  " , "Parry Chance: " , str(mod_hero_parry))
    
    enemy_damage = random.randint(1,4) #damage needs to be rolled in the loop otherwise it stays the same for the whole game
    hero_damage = random.randint(1,4)
    hero_hitchance = random.randint(1,100)
    mod_enemy_parrychance = random.randint(1,100)
    print("You attack and roll", hero_hitchance)

    if hero_hitchance < mod_hero_attack and mod_enemy_parrychance > mod_enemy_parry:
        print("You hit!", hero_hitchance)
        print("Enemy fails parry: " , mod_enemy_parrychance)
        enemy_health = enemy_health - hero_damage
        print("You do damage: " , hero_damage)
        print("Enemy health down to: " , enemy_health)
        
    if hero_hitchance < mod_hero_attack and mod_enemy_parrychance < mod_enemy_parry:
        print("You hit!", hero_hitchance)
        print("But the enemy PARRIES: " , mod_enemy_parrychance)
        print("Enemy health is still: " , enemy_health)
        
    if hero_hitchance > mod_hero_attack:
        print("You missed!")
        print("Enemy health is still: " , enemy_health)

    print("- - - - - - - - - -")
    time.sleep(1)
    print("Enemies turn to attack...")
    time.sleep(1)

    enemy_hitchance = random.randint(1,100)
    mod_hero_parrychance = random.randint(1,100)

    if enemy_hitchance < mod_enemy_attack and mod_hero_parrychance > mod_hero_parry:
        print("Enemy hits You!", enemy_hitchance)
        print("You fail to parry: " , mod_hero_parrychance)
        hero_health = hero_health - enemy_damage
        print("Enemy does damage: " , enemy_damage)
        print("Your health down to: " , hero_health)
        
    if enemy_hitchance < mod_enemy_attack and mod_hero_parrychance < mod_hero_parry:
        print("Enemy hits You!", enemy_hitchance)
        print("But the you PARRY: " , mod_hero_parrychance)
        print("Hero health is still: " , hero_health)
        
    if enemy_hitchance > mod_enemy_attack:
        print("Enemy missed you!")
        print("Your health is still: " , hero_health)
    print("****************")
    print("  ")
    
    time.sleep(3)
    
    if hero_health <= 0 or enemy_health <= 0 :
        if hero_health <=0 :
            print("YOU DIED")
        if enemy_health <=0 :
            print("You WIN")
        if hero_health <=0 and enemy_health <=0 :
            print("Both you and the enemy give each other fatal wounds with your last attack")
        break

