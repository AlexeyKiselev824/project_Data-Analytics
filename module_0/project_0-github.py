import numpy as np


def game_core_v2(number):
    """Function to guessing random numbers."""
    count = 1
    low = 1  # Lower search limit
    high = 101  # Search upper limit
    predict = np.random.randint(low, high)
    while number != predict:
        count += 1
        predict = (high + low) // 2
        if number > predict:
            low = predict
        elif number < predict:
            high = predict
    return count


def score_game(game_core):
    """Repeat 1000 times to determine the average number of attempts."""
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the number on average in {score} tries")
    return score


score_game(game_core_v2)