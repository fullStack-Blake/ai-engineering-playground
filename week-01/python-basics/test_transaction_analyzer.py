from transaction_analyzer import (
    calculate_total_spending, 
    find_largest_transaction,
    find_transactions_over_fifty,
)

# Pytest automatically discovers test functions whose names start with test_.
def test_calculate_total_spending():
    transactions = [
        {"merchant": "UPS", "amount": 10.0},
        {"merchant": "Canada Post", "amount": 20.0},
    ]
    assert calculate_total_spending(transactions) == 30.0


def test_calculate_total_spending_empty_transactions():
    transactions = []
    assert calculate_total_spending(transactions) == 0.0

def test_find_largest_transaction():
    transactions = [
        {"merchant": "UPS", "category" : "shipping", "amount": 10.0},
        {"merchant": "Canada Post", "category" : "shipping", "amount": 20.0}
    ]
    assert find_largest_transaction(transactions) == ["Canada Post", 20.0]

def test_find_transactions_over_fifty():
    transactions = [
        {"merchant": "UPS", "category" : "shipping", "amount": 10.0},
        {"merchant": "Canada Post", "category" : "shipping", "amount": 50.0},
        {"merchant": "Amazon", "category" : "shipping", "amount": 75.0},
    ]
    assert find_transactions_over_fifty(transactions) == [{"merchant": "Canada Post", "category" : "shipping", "amount": 50.0},
        {"merchant": "Amazon", "category" : "shipping", "amount": 75.0}]

def test_find_transactions_over_fifty_no_matches():
    transactions = [
        {"merchant": "UPS", "category" : "shipping", "amount": 10.0},
        {"merchant": "Canada Post", "category" : "shipping", "amount": 49.9},
    ]
    assert find_transactions_over_fifty(transactions) == []