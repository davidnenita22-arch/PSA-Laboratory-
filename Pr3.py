import random
import statistics

def play_labouchere(original: list[int], p_win: float = 18/38, max_steps: int = 5000) -> dict:
    """
    Simulate one full Labouchere session.
    Returns a dictionary with results.
    """
    line = original[:]
    original_sum = sum(original)
    profit = 0
    steps = 0
    max_bet = 0
    terminated = False

    while steps < max_steps and line:
        steps += 1

        # Determine bet
        if len(line) == 1:
            bet = line[0]
        else:
            bet = line[0] + line[-1]

        max_bet = max(max_bet, bet)

        # Simulate roulette spin
        if random.random() < p_win:
            # WIN
            profit += bet
            # Remove first and last
            if len(line) > 1:
                line = line[1:-1]
            else:
                line = []
        else:
            # LOSE
            profit -= bet
            line.append(bet)

    if not line:
        terminated = True
        # Verify the mathematical claim
        assert profit == original_sum, f"Math broken! Profit={profit}, expected={original_sum}"

    return {
        "terminated": terminated,
        "profit": profit,
        "steps": steps,
        "max_bet": max_bet,
        "final_list_length": len(line),
        "original_sum": original_sum
    }


def simulate_many(n_simulations: int = 2000, original: list[int] = [1, 2, 3, 4]):
    print(f"Original list : {original}  (target profit = ${sum(original)})")
    print(f"Simulations   : {n_simulations:,}\n")

    for p_win, label in [(0.5, "FAIR GAME (p=50% — theoretical)"),
                         (18/38, "REAL ROULETTE (American, p≈47.37%)")]:
        
        results = []
        for _ in range(n_simulations):
            res = play_labouchere(original, p_win=p_win)
            results.append(res)

        terminated = [r for r in results if r["terminated"]]
        profits = [r["profit"] for r in results]

        print(f"→ {label}")
        print(f"  Terminated successfully : {len(terminated):,} / {n_simulations:,} "
              f"({len(terminated)/n_simulations*100:5.1f}%)")
        print(f"  Average profit          : ${statistics.mean(profits):8.2f}")
        print(f"  Median profit           : ${statistics.median(profits):8.2f}")
        print(f"  Worst loss              : ${min(profits):8.2f}")
        print(f"  Biggest bet ever placed : ${max(r['max_bet'] for r in results):8,.0f}")
        print(f"  Avg steps per session   : {statistics.mean(r['steps'] for r in results):8,.0f}\n")


if __name__ == "__main__":
    random.seed(42)          # reproducible
    simulate_many()