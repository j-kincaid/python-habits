import random

# 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# print(names[0])
# i = int(len(names))

# card_toss = random.randint(0, i-1)
loser = random.choice(names)
print(f"{loser} is going to buy the meal today!")

