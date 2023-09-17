"""
Factorial of Factorials by Timothy Eden
Date Last Modified: September 17, 2023

This is my implementation of the following challenge from Edabit:
https://edabit.com/challenge/f3jX2BwzAuR8DXsy4
"""


def fact(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


def fact_of_fact(n):
    result = 1
    for num in range(2, n + 1):
        result *= fact(num)
    return result


def main():
    assert fact_of_fact(4) == 288
    assert fact_of_fact(1) == 1
    assert fact_of_fact(5) == 34560
    assert fact_of_fact(2) == 2
    assert fact_of_fact(6) == 24883200
    assert fact_of_fact(3) == 12
    assert fact_of_fact(14) == 69113789582492712943486800506462734562847413501952000000000000000
    assert fact_of_fact(11) == 265790267296391946810949632000000000
    assert fact_of_fact(7) == 125411328000
    assert fact_of_fact(13) == 792786697595796795607377086400871488552960000000000000
    assert fact_of_fact(8) == 5056584744960000
    assert fact_of_fact(10) == 6658606584104736522240000000
    assert fact_of_fact(9) == 1834933472251084800000
    assert fact_of_fact(12) == 127313963299399416749559771247411200000000000


if __name__ == '__main__':
    main()
