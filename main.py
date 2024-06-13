import random

# Define the suits and ranks of the cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Create and shuffle the deck
deck = [(rank, suit) for suit in suits for rank in ranks]
random.shuffle(deck)

def card_value(card):
    """Returns the value of a single card."""
    rank, suit = card
    if rank in ['Jack', 'Queen', 'King']:
        return 10
    elif rank == 'Ace':
        return 11
    else:
        return int(rank)

def calculate_hand_value(hand):
    """Calculates the total value of a hand of cards."""
    value = sum(card_value(card) for card in hand)
    num_aces = sum(1 for card in hand if card[0] == 'Ace')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def player_turn(deck, player_hand):
    """Handles the player's turn."""
    while True:
        print(f"Your hand: {player_hand}, current value: {calculate_hand_value(player_hand)}")
        choice = input("Do you want to [H]it or [S]tand? ").lower()
        if choice == 'h':
            player_hand.append(deck.pop())
            if calculate_hand_value(player_hand) > 21:
                print(f"You bust! Final hand: {player_hand}, value: {calculate_hand_value(player_hand)}")
                return False
        elif choice == 's':
            return True

def dealer_turn(deck, dealer_hand):
    """Handles the dealer's turn."""
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    print(f"Dealer's hand: {dealer_hand}, value: {calculate_hand_value(dealer_hand)}")
    return calculate_hand_value(dealer_hand) <= 21

def determine_winner(player_hand, dealer_hand):
    """Determines the winner of the game."""
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    if player_value > 21:
        return "Dealer wins!"
    elif dealer_value > 21 or player_value > dealer_value:
        return "Player wins!"
    elif player_value < dealer_value:
        return "Dealer wins!"
    else:
        return "It's a tie!"

def main():
    """Main game loop."""
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    if player_turn(deck, player_hand):
        if dealer_turn(deck, dealer_hand):
            print(determine_winner(player_hand, dealer_hand))
        else:
            print("Dealer busts! Player wins!")
    else:
        print("Dealer wins!")

if __name__ == "__main__":
    main()
