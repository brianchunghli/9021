# Written by Eric Martin for COMP9021


'''
Generates an initial segment of the list of prime numbers based on
Euler sieveswitching between sets and sorted lists for a more effective
implementation.
'''


from input_output import *


def generate_primes():
    print('I will generate all prime numbers in the range [2, n] '
          'for the n of your choice.'
         )
    nicely_display(*sequence_and_max_size_from(
                        sieve_of_primes_up_to(input_int(min_value=2)))
                                              )


def sieve_of_primes_up_to(n):
    sieve = list(range(2, n + 1))
    i = -1
    k = -1
    while k:
        k = 0
        i += 1
        sieve_as_set = set(sieve)
        while (factor := sieve[i] * sieve[i + k]) <= n:
            sieve_as_set.remove(factor)
            k += 1
        sieve = sorted(sieve_as_set)
    return sieve


def sequence_and_max_size_from(sieve):
    return sieve, len(str(sieve[-1]))


if __name__ == '__main__':
    generate_primes()
