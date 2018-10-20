#!/usr/bin/env python2.7

"""
Implementation of expectation maximization algorithm on the coin-toss example. 

Inspired by the following work:
https://pdfs.semanticscholar.org/presentation/49a2/d769df4592fab60a324f3c6eed7e4a512a8c.pdf
https://ibug.doc.ic.ac.uk/media/uploads/documents/expectation_maximization-1.pdf
"""

__author__ = "C.S."


# Coin tosses. Each row represents a sequence of tosses with a specific coin.
tosses = [
    'HTTTHHTHTH',
    'HHHHTHHHHH',
    'HTHHHHHTHH',
    'HTHTTTHHTT',
    'THHHTHHHTH',
]

# Initial theta params (i.e. biases for head toss) for coins A and B
theta_A = 0.6
theta_B = 0.5

round_ctr = 0
theta_changed = True # boolean to break the loop
MIN_CHANGE = 1e-3 # minimum amount of update required for thetas to stay in the loop

print 'Tosses:',tosses
print 'Initial', 'Theta A:', theta_A, '- Theta B:', theta_B

while theta_changed:

    round_ctr += 1

    # Total expected heads (or tails) for coin A (or B) given theta_A (or B)
    total_e_heads_A = 0.
    total_e_tails_A = 0.
    total_e_heads_B = 0.
    total_e_tails_B = 0.

    # ===================
    # Expectation step
    # ===================

    for coin in tosses:
        
        heads_count = coin.count('H')
        tails_count = coin.count('T')

        # Probability of getting this sequence of toss with coin A (or B)
        binom_A = (theta_A ** heads_count) * ((1 - theta_A) ** tails_count)
        binom_B = (theta_B ** heads_count) * ((1 - theta_B) ** tails_count)

        # Given this sequence, probability that it is coin A (or B)
        prob_A = (binom_A) / (binom_A + binom_B)
        prob_B = (binom_B) / (binom_A + binom_B)

        # Expected heads (or tails) for coin A (or B) given prob_A (or B) based on this sequence
        e_heads_A = prob_A * heads_count
        e_tails_A = prob_A * tails_count

        e_heads_B = prob_B * heads_count
        e_tails_B = prob_B * tails_count

        # Expected heads (or tails) for coin A (or B) given prob_A (or B) across all sequences
        total_e_heads_A += e_heads_A
        total_e_tails_A += e_tails_A
        total_e_heads_B += e_heads_B
        total_e_tails_B += e_tails_B

    # ===================
    # Maximization step
    # ===================

    # Update theta_A (and B)
    theta_A_last = theta_A
    theta_B_last = theta_B
    theta_A = total_e_heads_A / (total_e_heads_A + total_e_tails_A)
    theta_B = total_e_heads_B / (total_e_heads_B + total_e_tails_B)

    # If no change in the parameters, break the loop
    if abs(theta_A_last - theta_A) < MIN_CHANGE and abs(theta_B_last - theta_B) < MIN_CHANGE:
        theta_changed = False

    print 'Round: %d - Theta A: %.2f - Theta B: %.2f' % (round_ctr, theta_A, theta_B)
    
print 'Done.'      
