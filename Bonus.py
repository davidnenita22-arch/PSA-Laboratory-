import random
from PIL import Image

#  Configuration 
IMAGE_PATH      = "Bonus1.png"   # put the image in the same folder, or use full path
TOTAL_SQ_MILES  = 42             # given in the problem
NUM_SAMPLES     = 1_000_000      # more samples → more accurate

#  Red pixel detection 
def is_red(r, g, b):
    return r > 150 and g < 80 and b < 80

#  Load image
img    = Image.open(IMAGE_PATH).convert("RGB")
width, height = img.size
pixels = img.load()

print(f"  Image size    : {width} x {height} px")
print(f"  Total area    : {TOTAL_SQ_MILES} sq miles")
print(f"  Samples       : {NUM_SAMPLES:,}")
print()

# ── Monte Carlo sampling 
red_hits = 0

for _ in range(NUM_SAMPLES):
    x = random.randint(0, width  - 1)
    y = random.randint(0, height - 1)
    r, g, b = pixels[x, y]
    if is_red(r, g, b):
        red_hits += 1

# ── Results ──────
red_fraction = red_hits / NUM_SAMPLES
red_area     = red_fraction * TOTAL_SQ_MILES

print(f"  Red hits      : {red_hits:,} / {NUM_SAMPLES:,}")
print(f"  Red fraction  : {red_fraction:.4%}")
print(f"  Estimated red area: {red_area:.4f} sq miles")
print("=" * 55)

#  Cross-check: exact pixel count for reference 
total_pixels = width * height
red_pixels   = sum(
    1 for y in range(height) for x in range(width)
    if is_red(*pixels[x, y])
)
exact_fraction = red_pixels / total_pixels
exact_area     = exact_fraction * TOTAL_SQ_MILES

print()
print("  Cross-check (exact pixel count):")
print(f"  Red pixels    : {red_pixels:,} / {total_pixels:,}")
print(f"  Red fraction  : {exact_fraction:.4%}")
print(f"  Exact red area: {exact_area:.4f} sq miles")
print("=" * 55)