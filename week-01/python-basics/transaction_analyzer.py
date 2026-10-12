# strip removes \n from the row
# split separates values by provided delimiter
def csv_to_transactions(filename):
    transactions = []
    with open(filename) as file:
        data = file.readlines()
        for line in data[1:]:
            merchant, category, amount = line.strip().split(",")
            transaction = {
                "merchant" : merchant,
                "category" : category,
                "amount" : float(amount)
            }
            transactions.append(transaction)
    return transactions

def find_largest_transaction(transactions):
    largest_transaction = 0
    largest_merchant = ""
    for transaction in transactions:
        if transaction["amount"] > largest_transaction:
            largest_transaction = transaction["amount"]
            largest_merchant = transaction["merchant"]
    return [largest_merchant, largest_transaction]


def calculate_total_spending(transactions):
    total_spending = 0
    for transaction in transactions:
        total_spending += transaction["amount"]
    return total_spending

def find_transactions_over_fifty(transactions):
    transactions_over_fifty = []
    for transaction in transactions:
        if transaction["amount"] >= 50:
            transactions_over_fifty.append(transaction)
    return transactions_over_fifty

def main():
    transactions = csv_to_transactions("./transactions.csv")
    total_spending = calculate_total_spending(transactions)
    largest_merchant, largest_transaction = find_largest_transaction(transactions)
    transaction_equal_or_over_fifty = find_transactions_over_fifty(transactions)

    print(transactions)
    print(f"Total spending: ${total_spending}")
    print(f"Largest transaction: {largest_merchant} - ${largest_transaction}")

    print("Transactions >= 50:")
    for row in transaction_equal_or_over_fifty:
        print(row)
    
    print(f"Testing Assert")
    
    new_transactions = [
        {"merchant": "UPS", "category" : "shipping", "amount": 10.0},
        {"merchant": "Canada Post", "category" : "shipping", "amount": "invalid"}
    ]
    try:
        assert calculate_total_spending(new_transactions) == 30.0
    except TypeError as error:
        print(error)
    
    try:
        calculate_total_spending(new_transactions)
    except TypeError:
        print(f"Invalid transaction amount")
    print(f"and continues")

if __name__ == "__main__":
    main()