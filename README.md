# expectation-maximization
A small project to practice the EM concepts and the coin toss example.

Inspired by the following work:

http://ai.stanford.edu/~chuongdo/papers/em_tutorial.pdf
https://pdfs.semanticscholar.org/presentation/49a2/d769df4592fab60a324f3c6eed7e4a512a8c.pdf
https://ibug.doc.ic.ac.uk/media/uploads/documents/expectation_maximization-1.pdf

## Objective
The goal is to estimate biases for tossing heads for a couple of coins. We start with some initial biases for both coins (0.6 and 0.5). We have multiple (5) sequences of coin tosses, each sequence (of 10) is done by a specific coin but we don't know which coin. The coins are latent variables.

## Algorithm Overview
We take the following approach:
Consider a sequence of tosses by a coin. Count the number of heads and tails.

#### Expectation:
    Calculate the probability of getting this sequence if this is coin A.
    Calculate the probability of getting this sequence if this is coin B.
    Given above probabilities, calculate the probability that this is coin A.
    Given above probabilities, calculate the probability that this is coin B.
    Use the above probabilities to calculate the expected number of heads and tails for each coin, for this sequence:
        expected number of head tosses for coin A = Probability that this is A * number of head tosses in this sequence
        expected number of tail tosses for coin A = Probability that this is A * number of tail tosses in this sequence
        expected number of head tosses for coin B = Probability that this is A * number of head tosses in this sequence
        expected number of tail tosses for coin B = Probability that this is A * number of tail tosses in this sequence

Do this across all sequences, keep track of total expected heads and tails for coins A and B.

#### Maximization:
    Use the total expected heads and tails for coins A and B to re-calculate the biases for A and B:
        bias for heads of coin A = expected heads for A / (expected heads for A + expected tails for A)
        bias for heads of coin A = expected heads for B / (expected heads for B + expected tails for B)

Repeat as long as the biases change.


