# Good morning! Here's your coding interview problem for today.

# This problem was asked by Two Sigma.

# Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple probabilistic games.

# The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your number of rolls is the amount you pay, in dollars.

# The second game: same, except that the stopping condition is a five followed by a five.

# Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games and calculate their expected value.

from random import randint

def test_game(mode: str, n=100000):
    "Test the games"
    
    rolls = 0
    for i in range(n):
        rolls += play_game(mode)
    
    return rolls/n

def play_game(mode: str):
    "Play either the first or second game"

    # roll a die repeatedly until you get 5, 6 in sequence
    history = [0, 0] 

    # while two last rolls arent 5, 6: roll
    if mode == '1':
        while history[-2:] != [5, 6]:
            history.append(randint(1, 6))
    elif mode == '2':
        while history[-2:] != [5, 5]:
            history.append(randint(1, 6))

    # return rolls - 2 junk values
    return len(history)-2

if __name__ == "__main__":

    # to test which is the better option, we will just do a test to see which one is larger
    # as the sample size of tests tends to +infinity
    # but since all dices are sampling wth replacement, they should (and probably will)
    # be equally probable in the long run, but unpredictable at single instances.

    res_1 = test_game("1")
    res_2 = test_game("2")
    print(f"Avg Game 1 cost: {res_1}, Avg Game 2 cost: {res_2}")
    # Prints: Avg Game 1 cost: 35.98446, Avg Game 2 cost: 42.09445
    # in roughly 6.2s on a bad cpu