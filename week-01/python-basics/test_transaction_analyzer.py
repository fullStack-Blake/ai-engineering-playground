from transaction_analyzer import calculate_total_spending

def test_calculate_total_spending():
    transactions = [
        {"merchant": "UPS", "amount": 10.0},
        {"merchant": "Canada Post", "amount": 20.0},
    ]
    assert calculate_total_spending(transactions) == 30.0


def test_calculate_total_spending_empty_transactions():
    transactions = []
    assert calculate_total_spending(transactions) == 0.0