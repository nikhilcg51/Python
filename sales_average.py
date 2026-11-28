def calculate_average(sales):
    if not sales:
        return 0
    return round(sum(sales) / len(sales), 2)


def count_transactions(sales):
    return len(sales)