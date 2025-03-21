# A program that uses an API to print out 5 cards.
# It must print the value and suit of each card.
# Check if the user has drawn a pair, triple, straight or all of the same suit and congratulate the user.
# Author: Joanna Kelly

import requests
from collections import Counter

# Get a shuffled deck and draw 5 cards
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url)
data = response.json()

deck_id = data["deck_id"]
count = 5

draw_card = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}"
response2 = requests.get(draw_card)
results = response2.json()

# Extract values and suits and put them in a list for counting, assign numerical values to cards in dict
values = []
suits = []

value_map = {"ACE": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                  "9": 9, "10": 10, "JACK": 11, "QUEEN": 12, "KING": 13}


for card in results["cards"]:
    values.append(card['value'])
    suits.append(card['suit'])
    print(f"{card ['value']} of {card['suit']}")

# Collect our values and counting them
value_counts = Counter(values)

# Transforming card values into numbers, sorting them numerically and storing them in num_values
num_values = sorted([value_map[v] for v in values])

# Looping through each value in value_counts to check whether certain parameters are met
for count in value_counts.values():
    if count == 5:
        print("Congratulations! You got a flush!")
    elif count == 3:
        print("Congratulations! You got a triple!")
    elif count == 2:
        print("Congratulations! You got a pair")
    elif all(num_values[i] + 1 == num_values[i + 1] for i in range(len(num_values) - 1)):
        print("Congratulations! You got a straight!")

#print("Card values:", values)
#print("Card suits:", suits)