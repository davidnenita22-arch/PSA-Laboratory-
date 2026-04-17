import random
import statistics

def play_one_game() -> tuple[int, float]:
    """
    Simulate a single round of the St. Petersburg game.
    Flip a fair coin until heads appears.
    If heads first appears on toss j → payout = 2^j dollars.
    Returns:
        (j, payout): toss number and dollar winnings
    """
    j = 1
    while random.random() > 0.5:  
        j += 1
    payout = 2 ** j
    return j, payout


def simulate(n_games: int) -> list[float]:
    """
    Play the game n_games times and return all payouts.
    """
    return [play_one_game()[1] for _ in range(n_games)]


def summarise(payouts: list[float], fee: float, label: str) -> None:
    """
    Print a statistical summary for a set of simulated payouts.
    """
    n = len(payouts)
    avg = statistics.mean(payouts)
    med = statistics.median(payouts)
    max_pay = max(payouts)
    net = avg - fee
    pct_beat = sum(1 for p in payouts if p > fee) / n * 100
    print(f"\n{'─'*55}")
    print(f" {label}")
    print(f"{'─'*55}")
    print(f" Games played : {n}")
    print(f" Entry fee : {fee:}$")
    print(f" Average payout : {avg}$")
    print(f" Median payout : {med}$" )
    print(f" Maximum payout : {max_pay}$")
    print(f" Net profit per game : {net:.1f}$")
    print(f" Games that beat fee : {pct_beat:.1f}%")


def reasonable_fee(payouts: list[float]) -> float:
    """
    Estimate a 'reasonable' fee as the median payout.
    The median represents what a typical player actually wins —
    half the time you'll beat it, half the time you won't.
    """
    return statistics.median(payouts)



def fee_vs_plays() -> None:
    """
    Show how the average (and thus the 'fair' fee) changes
    as you're allowed to play more and more games.
    """
    play_counts = [10, 50, 100, 500, 1_000, 5_000, 10_000, 50_000]
    n_trials = 20  # repeat each count to reduce noise
    print("\n" + "═"*55)
    print(" HOW REASONABLE FEE DEPENDS ON NUMBER OF PLAYS")
    print("═"*55)
    print(f" {'# Games':>10} {'Avg of avgs':>13} {'Typical median':>15}")
    print(f" {'─'*10} {'─'*13} {'─'*15}")
    for n in play_counts:
        trial_avgs = []
        trial_medians = []
        for _ in range(n_trials):
            payouts = simulate(n)
            trial_avgs.append(statistics.mean(payouts))
            trial_medians.append(statistics.median(payouts))
        avg_of_avgs = statistics.mean(trial_avgs)
        avg_median = statistics.mean(trial_medians)
        print(f" {n:>10,} ${avg_of_avgs:>12.2f} ${avg_median:>14.2f}")
    print(f"\n → The median stays near $2–$4 regardless of plays.")
    print(f" → The average grows with more plays (rare big wins),")
    print(f" confirming the paradox: expected value → ∞.")


def main():
    random.seed(42)  # reproducible results

    #  Scenario A: Short run (10 games) 
    payouts_10 = simulate(10)
    fee_10 = reasonable_fee(payouts_10)
    summarise(payouts_10, fee=fee_10, label="Scenario A — 10 games")

    #  Scenario B: Medium run (1,000 games)     payouts_1k = simulate(1_000)
    fee_1k = reasonable_fee(payouts_1k)
    summarise(payouts_1k, fee=fee_1k, label="Scenario B — 1,000 games")

    #  Scenario C: Large run (100,000 games) 
    payouts_100k = simulate(100_000)
    fee_100k = reasonable_fee(payouts_100k)
    summarise(payouts_100k, fee=fee_100k, label="Scenario C — 100,000 games")

    #  How fee changes with number of plays     fee_vs_plays()

    #  Final conclusion 
    print("\n" + "═"*55)
    print(" CONCLUSION")
    print("═"*55)
    print("""
Despite the infinite theoretical expected value,
people would realistically be willing to pay only about $2-$15 to play the St. 
Petersburg game, depending on how many times they are allowed to play.
    """)


if __name__ == "__main__":
    main()