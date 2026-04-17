def simulate_oscars_grind(spin_results: list[bool]) -> None:
    print("=" * 65)
    print(f"{'Spin':<6} {'Outcome':<10} {'Bet':>6} {'Seq Profit':>12} {'Total Profit':>13}")
    print("=" * 65)

    bet = 1
    seq_profit = 0.0
    total_profit = 0.0
    sequence = 1

    for i, win in enumerate(spin_results, start=1):
        outcome_str = "WIN  ✓" if win else "LOSS ✗"

        # Record bet BEFORE outcome
        current_bet = bet

        if win:
            seq_profit += bet
            total_profit += bet

            if seq_profit >= 1:
                print(f"{i:<6} {outcome_str:<10} {current_bet:>6} {seq_profit:>12.1f} {total_profit:>13.1f}  ← sequence {sequence} complete!")
                # Sequence complete — reset
                seq_profit = 0
                bet = 1
                sequence += 1
                continue
            else:
                # Increase bet by 1, but cap so we don't overshoot +1
                next_bet = bet + 1
                if seq_profit + next_bet > 1:
                    bet = round(1 - seq_profit)  # exact amount needed
                    bet = max(1, bet)
                else:
                    bet = next_bet
        else:
            total_profit -= bet
            seq_profit -= bet
            # On loss, bet stays the same
            

        print(f"{i:<6} {outcome_str:<10} {current_bet:>6} {seq_profit:>12.1f} {total_profit:>13.1f}")

    print("=" * 65)
    print(f"\nFinal total profit/loss after {len(spin_results)} spins: {total_profit:+.1f} units")
    print(f"Sequences completed: {sequence - 1}")


def generate_alternating_streaks(streak_length: int, num_streaks: int) -> list[bool]:
    """
    Generate alternating win/loss streaks.
    First streak = wins, second = losses, third = wins, ...
    """
    results = []
    for s in range(num_streaks):
        outcome = (s % 2 == 0)  # True on even streaks (wins), False on odd (losses)
        results.extend([outcome] * streak_length)
    return results



# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":

    # Example 1: Alternating streaks of 4 (W W W W L L L L W W W W ...)
    print("\n── Example 1: Alternating streaks of 4 (8 streaks) ──\n")
    spins = generate_alternating_streaks(streak_length=4, num_streaks=8)
    print("Spin sequence:", ["W" if s else "L" for s in spins])
    print()
    simulate_oscars_grind(spins)

    # Example 2: Brutal losing streak then recovery
    print("\n── Example 2: 8 losses then 8 wins ──\n")
    spins2 = [False] * 8 + [True] * 8
    print("Spin sequence:", ["W" if s else "L" for s in spins2])
    print()
    simulate_oscars_grind(spins2)

    # Example 3: Custom — you can define any sequence of W/L
    print("\n── Example 3: Custom sequence ──\n")
    custom = [True, False, True, True, False, False, False, True, True, True]
    print("Spin sequence:", ["W" if s else "L" for s in custom])
    print()
    simulate_oscars_grind(custom)