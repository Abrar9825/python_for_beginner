def fact_iter(n):
    fact = 1
    for i in range(n):
        fact = fact*(i+1)
    return fact


print(fact_iter(5))
