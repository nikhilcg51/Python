def calculate_average(sales):
    if not sales:
        return 0
    return sum(sales) / len(sales)


assert calculate_average([100, 200, 300, 400, 500]) == 300
assert calculate_average([]) == 0
assert calculate_average([500]) == 500

print("All tests passed!")