import re

phone_number=["    +38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11   "]

def normalize_phone(phone_number):
    # Remove all non-digit characters
    digits = re.sub(r'\D', '', phone_number)
    
    # Check if the number starts with '38' and has 12 digits
    if digits.startswith('38') and len(digits) == 12:
        return '+' + digits
    # Check if the number starts with '0' and has 10 digits:
    elif digits.startswith('0') and len(digits) == 10:
        return '+38' + digits
    else:
        return None

sanitized_numbers = [normalize_phone(num) for num in phone_number]
print("Normalize_phone_number :", sanitized_numbers)

