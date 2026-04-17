from fractions import Fraction


def analyze_roulette(num_slots: int, adjacent: bool) -> dict:
    num_bullets = 2
    num_safe    = num_slots - num_bullets   # how many empty (safe) chambers exist

    #  CASE 1: Spin the barrel before the 2nd pull 
    # Spinning resets everything. Each slot is equally likely.
    # Probability of landing on a safe slot = safe_slots / total_slots
    p_survive_spin = Fraction(num_safe, num_slots)

    # CASE 2: Pull without spinning 
    # The first pull was safe, so we KNOW the first slot fired was empty.
    # That leaves (num_slots - 1) unfired slots. Of those, how many are safe?
    # The answer depends on whether bullets are adjacent or not.

    remaining_slots = num_slots - 1          # one slot already fired (was safe)

    if adjacent:
        # Adjacent bullets 
        # Label the slots 1..N with bullets at positions 1 and 2.
        # If the barrel is spun randomly and we get a safe click,
        # the fired slot must have been one of the (num_safe) safe slots.
        #
        # Key insight: once we know a safe slot was fired,
        # the NEXT slot in the rotation is now the current chamber.
        # We need to count how many of those "next slots" are safe.
        #
        # Enumerate all possible fired positions and check the next one:
        slots = list(range(1, num_slots + 1))

        # Mark which slots are bullets (positions 1 and 2 = adjacent pair)
        bullet_positions = {1, 2}

        safe_fired_slots = [s for s in slots if s not in bullet_positions]

        # For each safe fired slot, what is the NEXT slot in the cylinder?
        next_slots_after_safe_fire = [
            (s % num_slots) + 1 for s in safe_fired_slots
        ]

        # Count how many of those next slots are also safe
        safe_next = sum(
            1 for s in next_slots_after_safe_fire if s not in bullet_positions
        )

        # P(survive | no spin, adjacent) = safe next slots / total safe fired slots
        p_survive_nospin = Fraction(safe_next, len(safe_fired_slots))

    else:
        # Non-adjacent bullets 
        # Bullets are spread out (not neighbors). Place them at positions 1
        # and ceil(N/2)+1 to guarantee non-adjacency.
        import math
        bullet_positions = {1, math.ceil(num_slots / 2) + 1}

        slots = list(range(1, num_slots + 1))
        safe_fired_slots = [s for s in slots if s not in bullet_positions]

        next_slots_after_safe_fire = [
            (s % num_slots) + 1 for s in safe_fired_slots
        ]

        safe_next = sum(
            1 for s in next_slots_after_safe_fire if s not in bullet_positions
        )

        p_survive_nospin = Fraction(safe_next, len(safe_fired_slots))

    # Recommendation
    if p_survive_nospin > p_survive_spin:
        recommendation = "Do not spin"
    elif p_survive_spin > p_survive_nospin:
        recommendation = "Spin"
    else:
        recommendation = "Both choices are equal"

    return {
        "num_slots":          num_slots,
        "adjacent":           adjacent,
        "p_survive_spin":     p_survive_spin,
        "p_survive_nospin":   p_survive_nospin,
        "recommendation":     recommendation,
    }


def print_results(results: dict) -> None:
    """Pretty-print a single scenario result."""
    adj_label = "Adjacent bullets" if results["adjacent"] else "Non-adjacent bullets"
    spin_pct  = float(results["p_survive_spin"])  * 100
    nospin_pct= float(results["p_survive_nospin"])* 100

    print(f"  {adj_label}")
    print(f"    Spin first : {results['p_survive_spin']} = {spin_pct:.2f}%")
    print(f"    No spin : {results['p_survive_nospin']} = {nospin_pct:.2f}%")
    print(f"    Recommendation: {results['recommendation']}")
    print()


def main():

    scenarios = [
        (6, True),   # 6-slot, adjacent
        (6, False),  # 6-slot, non-adjacent
        (5, True),   # 5-slot, adjacent
        (5, False),  # 5-slot, non-adjacent
    ]

    current_slots = None
    for num_slots, adjacent in scenarios:
        if num_slots != current_slots:
            current_slots = num_slots
            print(f"\n {num_slots} - slot revolver ")

        results = analyze_roulette(num_slots, adjacent)
        print_results(results)
        
    print(f"  {'Scenario':<35} {'Spin':>8} {'No Spin':>10} {'Best':>20}")
    print(f"  {'-'*35} {'-'*8} {'-'*10} {'-'*20}")
    for num_slots, adjacent in scenarios:
        r = analyze_roulette(num_slots, adjacent)
        adj_label = "adjacent" if adjacent else "non-adjacent"
        label = f"{num_slots}-slot, {adj_label}"
        spin_pct   = f"{float(r['p_survive_spin'])*100:.1f}%"
        nospin_pct = f"{float(r['p_survive_nospin'])*100:.1f}%"
        print(f"  {label:<35} {spin_pct:>8} {nospin_pct:>10} {r['recommendation']:>20}")

    print()


if __name__ == "__main__":
    main()