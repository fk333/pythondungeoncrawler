import random

hero_attack = 70
hero_parry = 40
hero_health = 10
enemy_attack = 70
enemy_parry = 40
enemy_health = 10
att_stance = 10 #increase att chance by 10% #reduce parry by 10%
def_stance = 10 #increase parry chance by 10% #reduce att by 10%
reckless_stance = 2


action = input("Press 1 to ATTACK or 2 for PARRY: ")
print("You chose", action)

#loop should start before hit chances are rolled

while True :
    enemy_damage = random.randint(1,4) #damage needs to be rolled in the loop otherwise it stays the same for the whole game
    hero_damage = random.randint(1,4)
    hero_hitchance = random.randint(1,100)
    enemy_parrychance = random.randint(1,100)
    print("You attack and roll", hero_hitchance)

    if hero_hitchance < hero_attack and enemy_parrychance > enemy_parry:
        print("You hit!", hero_hitchance)
        print("Enemy fails parry: " , enemy_parrychance)
        enemy_health = enemy_health - hero_damage
        print("You do damage: " , hero_damage)
        print("Enemy health down to: " , enemy_health)
        
    if hero_hitchance < hero_attack and enemy_parrychance < enemy_parry:
        print("You hit!", hero_hitchance)
        print("But the enemy PARRIES: " , enemy_parrychance)
        print("Enemy health is still: " , enemy_health)
        
    if hero_hitchance > hero_attack:
        print("You missed!")
        print("Enemy health is still: " , enemy_health)


    print("Enemies turn to attack...")

    enemy_hitchance = random.randint(1,100)
    hero_parrychance = random.randint(1,100)

    if enemy_hitchance < enemy_attack and hero_parrychance > hero_parry:
        print("Enemy hits You!", enemy_hitchance)
        print("You fail to parry: " , hero_parrychance)
        hero_health = hero_health - enemy_damage
        print("Enemy does damage: " , enemy_damage)
        print("Your health down to: " , hero_health)
        
    if enemy_hitchance < enemy_attack and hero_parrychance < hero_parry:
        print("Enemy hits You!", enemy_hitchance)
        print("But the you PARRY: " , hero_parrychance)
        print("Hero health is still: " , hero_health)
        
    if enemy_hitchance > enemy_attack:
        print("Enemy missed you!")
        print("Your health is still: " , hero_health)
    print("****************")
    print("  ")
    
    if hero_health <= 0 or enemy_health <= 0 :
        if hero_health <=0 :
            print("YOU DIED")
        if enemy_health <=0 :
            print("You WIN")
        if hero_health <=0 and enemy_health <=0 :
            print("Both you and the enemy give each other fatal wounds with your last attack")
        break

