import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
names_lenght = len(names)
random_number = random.randint(0, names_lenght-1)
print(f"{names[random_number]} is paying todays meal")
