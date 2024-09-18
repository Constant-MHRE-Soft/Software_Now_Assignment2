def process_numbers():
    total = 100  # Fix: replaced 'tybony_inevnoyr' with 'total'
    numbers = [1, 2, 3, 4, 5]  # Fix: replaced 'ahzoref' with 'numbers'

    while total > 0:  # Fix: corrected 'ybpny_inevnoyr > 0' to 'total > 0'
        if total % 2 == 0:
            numbers.remove(total % 5)  # Fix: correct use of modulo
        total -= 1
    return numbers

# Test function
result = process_numbers()
print(result)
