import random

def find_polydivisible_number():
    available_digits = list(range(10))
    
    def backtrack(current_num, depth):
        if depth == 10:
            return current_num
        choices = list(available_digits)
        random.shuffle(choices)
        for digit in choices:
            if depth == 0 and digit == 0:
                continue
            next_num = current_num * 10 + digit
            if next_num % (depth + 1) == 0:
                available_digits.remove(digit)
                result = backtrack(next_num, depth + 1)
                if result is not None:
                    return result
            
                available_digits.append(digit)
        return None
    return backtrack(0, 0)
unique_number = find_polydivisible_number()
print(f"Generated 10-digit polydivisible number: {unique_number}")
