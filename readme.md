# Probability Simulations & Cryptographic Attacks

This repository contains a series of laboratory works focused on probability theory, gambling paradoxes, and cybersecurity fundamentals. The projects utilize **Monte Carlo simulations** to analyze mathematical expectations and **cryptographic principles** to demonstrate hashing vulnerabilities.

## 📋 Table of Contents
1. [St. Petersburg Paradox](#1-st-petersburg-paradox)
2. [Russian Roulette Probability](#2-russian-roulette-probability)
3. [Labouchere Strategy](#3-labouchere-strategy)
4. [Oscar's Grind Strategy](#4-oscars-grind-strategy)
5. [MD5 Birthday Attack](#5-md5-birthday-attack)
6. [Bonus: Monte Carlo Map Integration](#bonus-monte-carlo-map-integration)

---

## 1. St. Petersburg Paradox
**Objective:** Determine a "fair" entry fee for a game with an infinite expected value.
- **The Game:** A coin is flipped until 'Heads' appears. You win $2^j$ dollars, where $j$ is the flip number.
- **Simulation:** This script runs thousands of iterations to find the average payout.
- **Key Insight:** Explores why the theoretical infinite value doesn't translate to real-world willingness to pay.

## 2. Russian Roulette Probability
**Objective:** Use Bayesian probability to make a life-saving decision.
- **Scenario:** Two bullets in adjacent slots of a 6-slot (and 5-slot) revolver. After one "Click," should you spin or pull?
- **Analysis:**
  - Case A: Adjacent bullets.
  - Case B: Non-adjacent bullets.
- **Outcomes:** The simulation outputs 8 distinct probability sets to determine the safest strategy.

## 3. Labouchere Strategy
**Objective:** Test the "Cancellation System" in Roulette.
- **Logic:** Follow a sequence (e.g., 1, 2, 3, 4). Bet the sum of the first and last numbers.
- **Simulation:** Tracks bankroll fluctuations and verifies if the system always results in a profit of the initial sum.
- **Analysis:** Demonstrates why table limits and bankroll exhaustion make this a "non-foolproof" system.

## 4. Oscar's Grind Strategy
**Objective:** Analyze a conservative progression system designed to withstand losing streaks.
- **Mechanism:** Aim for exactly 1 unit of profit per sequence. 
- **Evaluation:** Charts the evolution of bet sizes during winning/losing streaks to find the failure point of "Hoyle's Press."

## 5. MD5 Birthday Attack
**Objective:** Demonstrate a collision attack on the MD5 hashing algorithm.
- **Task:** Find two different inputs that produce the same first 40 bits (10 hex characters) of an MD5 hash.
- **Optimization:** Includes a 20-bit "fast mode" for initial verification before attempting the full 40-bit collision.

## 6. Bonus: Monte Carlo Map Integration
**Objective:** Estimate the surface area of mined regions (Red) on a CIA-provided map scan.
- **Parameters:** Total map area is 42 square miles.
- **Implementation:**
  - Uses the `Pillow` library to process image pixels.
  - Randomly samples coordinates to determine the ratio of "Mined" (Red) vs "Safe" pixels.
  - Computes the final area in square miles.

---

## 🛠 Installation & Usage

### Prerequisites
- Python 3.8+
- [Pillow](https://python-pillow.org/) (for map processing)

### Setup
```bash
# Clone the repository
git clone [https://github.com/your-username/repository-name.git](https://github.com/your-username/repository-name.git)

# Install dependencies
pip install Pillow