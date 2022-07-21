import random

hero_attack = 70
hero_parry = 40
hero_health = 10
hero_damage = 3
enemy_attack = 70
enemy_parry = 40
enemy_health = 10
enemy_damage = 3


action = input("Press 1 to ATTACK or 2 for PARRY: ")
print("You chose", action)

#loop should start before hit chances are rolled

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


