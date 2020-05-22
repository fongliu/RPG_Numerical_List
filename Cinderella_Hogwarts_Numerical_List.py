# RPG Numerical List -- Fong Liu
# This program will print out my RPG inventories in numerical list.



# Print what Cinderella wears to the ball in numerical list.
cinderella_outfit = ['headband', 'glass slippers', 'blue dress', 
                     'gloves', 'choker']
for outfit in cinderella_outfit:
    print(cinderella_outfit.index(outfit) + 1, f".", outfit)
    
# Print the the four Hogwarts houses in numerical list.
hogwarts_houses = ['Hufflepuff', 'Ravenclaw', 'Slytherin', 
                   'Gryffindor']
print(f"\n")
for house in hogwarts_houses:
    print(hogwarts_houses.index(house) + 1, f".", house)
