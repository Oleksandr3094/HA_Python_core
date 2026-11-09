import random

def get_numbers_ticket(min, max, quantity):
    if min<1 or max>1000 or quantity>(max-min) or quantity<1 or quantity>1000:
        return "Error"
    else:
        random_numbers = random.sample(range(min, max + 1), quantity)
        random_numbers.sort()
        return random_numbers

min = int(input("Enter the minimum number (1-1000): "))
max = int(input("Enter the maximum number (1-1000): "))
quantity = int(input("Enter the quantity of numbers to generate: "))

print(get_numbers_ticket(min, max, quantity))
