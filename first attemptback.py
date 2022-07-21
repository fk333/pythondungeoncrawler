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

hero_hitchance = random.randint(1,100)
enemy_parrychance = random.randint(1,100)
print("You attack and roll", hero_hitchance)

if hero_hitchance < hero_attack :
    print("You hit!", hero_hitchance)
    
    if enemy_parrychance > enemy_parry :
        print("Enemy succesfully parried." , enemy_parrychance)
    
    
    enemy_health = enemy_health - hero_damage
    print("You do damage: " , hero_damage)
    print("Enemy health down to: " , enemy_health)
else:
    print("You missed!")
    print("Enemy health is still: " , enemy_health)


