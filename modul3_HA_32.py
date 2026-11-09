import random

def get_numbers_ticket(min, max, quantity):
    if min<1 or max>1000 or quantity<(max-min) or quantity<1 or quantity>1000:
        return "Error"
    else:
        