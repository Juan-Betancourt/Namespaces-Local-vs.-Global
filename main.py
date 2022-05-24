################### Scope ####################

# Modifiying Global Scope

enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

increase_enemies()
print(f"enemies outside function: {enemies}")

# #Global Scope
# player_health = 10

# Local Scope

# def game():
#   def drink_potion():
#     potion_strength = 2
#     print(player_health)

#   drink_potion()

  
# print(player_health)

# There is no Block Scope

# game_level = 3
# def create_enemy():
#   enemies = ["Skeleton", "Zombie", "Alien"]
#   if game_level < 5:
#     new_enemy = enemies[0]

#   print(new_enemy)

# create_enemy()

