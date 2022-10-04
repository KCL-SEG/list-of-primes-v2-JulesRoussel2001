"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError(f"{number_of_primes} should have been a positive value.")
    else:
        list = []
        num = 2
        while len(list) < number_of_primes:
            count = 0
            for i in range(1,num):
                if num % i == 0:
                    count += 1
            if count == 1:
                list.append(num)
            num += 1
        return list
