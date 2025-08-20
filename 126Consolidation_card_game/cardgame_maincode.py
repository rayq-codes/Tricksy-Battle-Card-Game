import random

# Create a deck without Kings
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = list(range(1, 11)) + [11, 12]  # Ace = 1, J = 11, Q = 12
deck = [(v, s) for s in suits for v in values]
random.shuffle(deck)

# Deal 8 cards to each player
def deal_cards():
    hand = []
    for _ in range(8):
        card = deck.pop()
        hand.append(card)
    return hand

def card_str(card):
    face_cards = {1: 'Ace', 11: 'Jack', 12: 'Queen'}
    return f"{face_cards.get(card[0], str(card[0]))} of {card[1]}"

player1 = deal_cards()
player2 = deal_cards()
player1_points = 0
player2_points = 0
rounds_played = 0

leader = random.choice([0, 1])  # 0 = Player 1, 1 = Player 2

#Main game loop
while rounds_played < 16 and player1 and player2:
    print(f"\n** Round {rounds_played + 1} **")
    print(f"Your hand:")
    for i, card in enumerate(player1):
        print(f"{i+1}: {card_str(card)}")

    if leader == 0:
        # Player 1 (you) leads
        while True:
            try:
                choice = int(input("Choose a card to lead: ")) - 1
                lead_card = player1.pop(choice)
                break
            except (ValueError, IndexError):
                print("Invalid selection, try again.")

        matching = [c for c in player2 if c[1] == lead_card[1]]
        if matching:
            follow_card = matching[0]
            print(f"• Player 2 has a card in {lead_card[1]} and plays {card_str(follow_card)}.")
        else:
            follow_card = player2[0]
            print(f"• Player 2 has no {lead_card[1]} cards and plays {card_str(follow_card)} instead.")
        player2.remove(follow_card)

    else:
        # Player 2 leads
        lead_card = player2.pop(0)
        print(f"Player 2 leads by playing a {card_str(lead_card)}.")

        matching = [c for c in player1 if c[1] == lead_card[1]]
        if matching:
            print("• You must follow suit. Your options:")
            for i, card in enumerate(matching):
                print(f"{i+1}: {card_str(card)}")
            while True:
                try:
                    choice = int(input("Choose a card to follow: ")) - 1
                    follow_card = matching[choice]
                    break
                except (ValueError, IndexError):
                    print("Invalid selection, try again.")
        else:
            print("• You have no matching suit. Choose any card:")
            for i, card in enumerate(player1):
                print(f"{i+1}: {card_str(card)}")
            while True:
                try:
                    choice = int(input("Choose a card to play: ")) - 1
                    follow_card = player1[choice]
                    break
                except (ValueError, IndexError):
                    print("Invalid selection, try again.")
        player1.remove(follow_card)

    print(f"Leader played: {card_str(lead_card)}")
    print(f"Follower played: {card_str(follow_card)}")
    
    #calculate point winner
    if follow_card[1] == lead_card[1] and follow_card[0] > lead_card[0]:
        winner = 1 - leader
    else:
        winner = leader

    if winner == 0:
        player1_points += 1
        print("• Player 1 wins the point.")
    else:
        player2_points += 1
        print("• Player 2 wins the point.")

    leader = winner

    # Reveal a card from the deck
    if deck:
        revealed = deck.pop()
        print(f"• The players turn a card over from the deck to reveal a {card_str(revealed)}.")
    else:
        print("• No cards left in the deck to reveal.")

    # Deal 4 more cards if needed
    if len(player1) == 4 and len(player2) == 4 and len(deck) >= 8:
        print("Both players have 4 cards — dealing 4 more.")
        player1 += deal_cards()
        player2 += deal_cards()
    elif len(deck) < 8:
        print("Not enough cards left in the deck to deal more.")

    rounds_played += 1

    # Early end
    if (player1_points >= 9 and player2_points >= 1) or (player2_points >= 9 and player1_points >= 1):
        print("Game ended early — no way for opposing player to win.")
        break

# Final hand check for optional final deal
if len(player1) == 4 and len(player2) == 4 and len(deck) >= 8:
    print("Both players have 4 cards — dealing 4 more.")
    player1 += deal_cards()
    player2 += deal_cards()

# Shoot the moon rule
if player1_points == 0 and player2_points == 16:
    print("Player 2 shot the moon! Player 2 wins with 17 points!")
elif player2_points == 0 and player1_points == 16:
    print("Player 1 shot the moon! Player 1 wins with 17 points!")
else:
    print("\n*** Game Over ***")
    print(f"Player 1 points: {player1_points}")
    print(f"Player 2 points: {player2_points}")
    if player1_points > player2_points:
        print("Player 1 wins!")
    elif player2_points > player1_points:
        print("Player 2 wins!")
    else:
        print("It's a tie!")
