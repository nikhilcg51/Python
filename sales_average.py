def calculate_average(sales):
    if not sales:
        return 0
    return round(sum(sales) / len(sales), 3)