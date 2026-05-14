from fractions import Fraction


def analyze_roulette(num_slots: int, adjacent: bool) -> dict:
    num_bullets = 2
    num_safe = num_slots - num_bullets  # how many empty (safe) chambers exist
    
    p_survive_spin = Fraction(num_safe, num_slots)

    remaining_slots = num_slots - 1  # one slot already fired (was safe)

    if adjacent:
        slots = list(range(1, num_slots + 1)) 

        # Mark which slots are bullets (positions 1 and 2 = adjacent pair)
        bullet_positions = {1, 2}

        safe_fired_slots = [s for s in slots if s not in bullet_positions] #list chamber that are safe

        # For each safe fired slot, what is the next slot
        next_slots_after_safe_fire = [(s % num_slots) + 1 for s in safe_fired_slots]

        # Count how many of those next slots are also safe
        safe_next = sum(1 for s in next_slots_after_safe_fire if s not in bullet_positions)

        p_survive_nospin = Fraction(safe_next, len(safe_fired_slots))

    else:
        # Non-adjacent bullets 
        # and ceil(N/2)+1 to guarantee non-adjacency.
        import math
        bullet_positions = {1, math.ceil(num_slots / 2) + 1}

        slots = list(range(1, num_slots + 1)) 
        safe_fired_slots = [s for s in slots if s not in bullet_positions]

        next_slots_after_safe_fire = [(s % num_slots) + 1 for s in safe_fired_slots]

        safe_next = sum(1 for s in next_slots_after_safe_fire if s not in bullet_positions)

        p_survive_nospin = Fraction(safe_next, len(safe_fired_slots))

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
    spin_pct = float(results["p_survive_spin"])  * 100
    nospin_pct = float(results["p_survive_nospin"])* 100

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

    current_slots = None # Track when we switch from 6 to 5 slots to print a header
    for num_slots, adjacent in scenarios:
        if num_slots != current_slots:
            current_slots = num_slots
            print(f"\n {num_slots} - slot revolver ")

        results = analyze_roulette(num_slots, adjacent)
        print_results(results)

if __name__ == "__main__":  
    main()