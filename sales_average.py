def calculate_average(sales):
    if not sales:
        return 0
    return sum(sales) / len(sales)