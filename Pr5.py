from hashlib import sha1
from binascii import hexlify
from os import urandom

HASHCHARS = 10  # first 10 hex chars = 40 bits

def sha1_hash(s):
    if type(s) is bytes:
        return sha1(s).hexdigest()[:HASHCHARS]
    else:
        return sha1(s.encode('ascii')).hexdigest()[:HASHCHARS]

def show(orig_str, collision_str):
    orig_ascii    = orig_str.encode('ascii')
    collision_ascii = collision_str.encode('ascii')
    print('Collision found!')
    print(
        orig_str
        + ' (bytes: ' + str(hexlify(orig_ascii)) + ' )'
        + ' hashes to ' + str(sha1_hash(orig_ascii))
        + ', but ' + collision_str
        + ' (bytes: ' + str(hexlify(collision_ascii)) + ' )'
        + ' also hashes to ' + str(sha1_hash(collision_ascii))
    )

def is_collision(trial, orig_hash):
    return sha1_hash(trial) == orig_hash

def collide():
    # Pick a random starting message (8 random hex chars = readable ascii)
    orig = urandom(8).hex()          # e.g. 'a3f2c19d44b70e82'
    orig_hash = sha1_hash(orig)

    print(f'Looking for a collision with: "{orig}" (hash prefix: {orig_hash})')
    print('Searching...\n')

    # Birthday attack: store ALL seen hashes, not just one target.
    # Any two messages sharing a prefix = collision.
    # Expected attempts ~ 2^(HASHCHARS*4/2) = 2^20 ~ 1,000,000
    seen = {orig_hash: orig}
    attempts = 0

    while True:
        trial = urandom(8).hex()
        trial_hash = sha1_hash(trial)
        attempts += 1

        if trial_hash in seen and seen[trial_hash] != trial:
            # Found a collision — reuse show() with the stored original
            orig     = seen[trial_hash]
            orig_hash = trial_hash
            show(orig, trial)
            print(f'\nAttempts: {attempts:,}')
            break

        seen[trial_hash] = trial

        if attempts % 200_000 == 0:
            print(f'  ... {attempts:,} attempts so far')

collide()