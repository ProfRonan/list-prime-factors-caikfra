def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def list_prime_factors(number):
    factors = []
    divisor = 2

    while number > 1:
        if number % divisor == 0:
            factors.append(divisor)
            number = number / divisor
        else:
            divisor += 1

    return factors