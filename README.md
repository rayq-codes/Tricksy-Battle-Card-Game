#My Program
A programmed card game

#How to Run
Run using the Python command in your terminal or IDE

#What It Does
Assigns numbers to suit positions (Ace = 1, Jack = 11, Queen = 12).

Creates a deck of cards and randomizes/shuffles it using random.shuffle(deck).

Use print(deck) to check the shuffled deck.

Deals 8 cards to each player.

Use print(player1, player2) to verify the hands.

Initializes other variables such as player points and rounds played to 0.

Uses a while loop to run rounds:

The leader plays a card, the follower responds (matching suit if possible), and both hands update as the game progresses until all cards are played.

Determines the winner of each round based on suit and value, awards a point to the winner, and sets them as the next round leader.

Reveals a card from the deck and deals 4 new cards to each player if both have 4 cards remaining and the deck allows.

Increments the round counter, determines the winner, and prints final game results.

Implements an early game breaker: if one player reaches 9 points while the opponent has only 1, the game ends.

Includes full “ending the game” rules and bug fixes.

Me and a peer added user input, turn-by-turn narration, and round-by-round play, replacing the original randomizer that allowed all 16 rounds to be played at once.

