import random
import numpy as np

def play_game():
    """Flip coin until heads. Pay 2^j if heads on toss j."""
    j = 1
    while random.random() >= 0.5:  # tails
        j += 1
    return 2 ** j  # heads on toss j

def simulate(n_games):
    payouts = [play_game() for _ in range(n_games)]
    avg = np.mean(payouts)
    median = np.median(payouts)
    print(f"Games: {n_games:>7} | Avg payout: ${avg:>10.2f} | Median: ${median:.0f}")
    return avg

for n in [10, 100, 1000, 10000, 100000]:
    simulate(n)
    
    """ the average mean how much people should be willing to pay to play this game, 
    but the median is much lower, showing that most people will win a small amount, 
    while a few will win a huge amount, skewing the average. this is why the more games there are 
    the higher the average payout, because there's a greater chance of hitting those rare, large payouts.
    so a decent amount would be 2-4$ for few games and 12-20$ for more games"""
    
