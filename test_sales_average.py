from sales_average import calculate_average, count_transactions

assert calculate_average([100, 200, 300, 400, 500]) == 300
assert calculate_average([]) == 0
assert calculate_average([500]) == 500
assert calculate_average([10, 20, 40]) == 23.33
assert count_transactions([100, 200, 300]) == 3
assert count_transactions([]) == 0
print("All tests passed!")