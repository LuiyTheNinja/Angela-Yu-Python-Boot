import random

# Card values
deck = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "Jack": 10, "Queen": 10, "King": 10, "Ace": 11
}

# Create and shuffle a standard 52-card deck
deck_keys = list(deck.keys()) * 4
random.shuffle(deck_keys)


def pull_card():
    """Draw a card from the deck."""
    if not deck_keys:
        raise ValueError("The deck is empty!")

    card = deck_keys.pop()
    return card, deck[card]


def update_score(current_total, aces_count, new_card_val):
    """Update the score while handling Aces."""
    if new_card_val == 11:
        aces_count += 1

    current_total += new_card_val

    while current_total > 21 and aces_count > 0:
        current_total -= 10
        aces_count -= 1

    return current_total, aces_count


player_total = 0
dealer_total = 0
player_aces = 0
dealer_aces = 0

player_cards = []
dealer_cards = []

# Initial deal (2 cards each)
for _ in range(2):
    card, value = pull_card()
    player_cards.append(card)
    player_total, player_aces = update_score(player_total, player_aces, value)

    card, value = pull_card()
    dealer_cards.append(card)
    dealer_total, dealer_aces = update_score(dealer_total, dealer_aces, value)

# Check for Blackjack
if player_total == 21 and dealer_total == 21:
    print("\nBoth players have Blackjack! Push (Tie).")
    exit()
elif player_total == 21:
    print("\nBlackjack! You win!")
    exit()
elif dealer_total == 21:
    print("\nDealer has Blackjack! You lose!")
    exit()

# ---------------- PLAYER TURN ----------------
while True:
    print("\n----------------------------")
    print("Your cards:", ", ".join(player_cards))
    print("Your total:", player_total)
    print(f"Dealer shows: {dealer_cards[0]}")

    choice = input("\nHit or Stand? (h/s): ").strip().lower()

    if choice in ["h", "hit", "yes", "y"]:
        card, value = pull_card()
        player_cards.append(card)
        player_total, player_aces = update_score(player_total, player_aces, value)

        print(f"\nYou drew: {card}")

        if player_total > 21:
            print("\nYour cards:", ", ".join(player_cards))
            print("Total:", player_total)
            print("Bust! You lose.")
            exit()

        if player_total == 21:
            print("\nYou have 21!")
            break

    elif choice in ["s", "stand", "no", "n"]:
        break

    else:
        print("Invalid input. Please enter 'h' or 's'.")

# ---------------- DEALER TURN ----------------
print("\nDealer reveals:", ", ".join(dealer_cards))
print("Dealer total:", dealer_total)

while dealer_total < 17:
    card, value = pull_card()
    dealer_cards.append(card)
    dealer_total, dealer_aces = update_score(dealer_total, dealer_aces, value)

    print(f"Dealer draws: {card}")
    print("Dealer total:", dealer_total)

# ---------------- RESULTS ----------------
print("\n========== FINAL HANDS ==========")
print("Your cards:", ", ".join(player_cards))
print("Your total:", player_total)
print()
print("Dealer cards:", ", ".join(dealer_cards))
print("Dealer total:", dealer_total)

if dealer_total > 21:
    print("\nDealer busts! You win!")
elif player_total > dealer_total:
    print("\nYou win!")
elif dealer_total > player_total:
    print("\nDealer wins!")
else:
    print("\nIt's a tie (Push)!")