# A program that uses an API to print out 5 cards.
# It must print the value and suit of each card.
# Check if the user has drawn a pair, triple, straight or all of the same suit and congratulate the user.
# Author: Joanna Kelly

import requests

def draw_cards(count=5):
    url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    response = requests.get(url)
    data = response.json()

    deck_id = data["deck_id"]

    draw_card = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}"
    response2 = requests.get(draw_card)
    results = response2.json()

    values = []
    suits = []

    value_map = {"ACE": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
                  "9": 9, "10": 10, "JACK": 11, "QUEEN": 12, "KING": 13}


    for card in results["cards"]:
        values.append(card['value'])
        suits.append(card['suit'])
        #print(f"{card ['value']} of {card['suit']}")


print("Card values:", values)
print("Card suits:", suits)