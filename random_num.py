import random

random_num = random.randint(1, 6)
print("Random num from 1 to 6 is:", random_num)

my_list = ['rock', 'paper', 'scissors']
random_item = random.choice(my_list)
print("Random item is:", random_item)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
random.shuffle(cards)
print("Cards:", cards)
print("Cards after shuffled:", cards)
