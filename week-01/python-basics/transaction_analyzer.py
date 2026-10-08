with open("./transactions.csv") as file:
    data = file.readlines()
    transactions = []
    total_spending = 0
    largest_transaction = 0
    largest_merchant = ""
    transaction_equal_or_over_fifty = []

    # strip removes \n from the row
    # split separates values by provided delimiter
    for row in data[1:]:
        merchant, category, amount = row.strip().split(",")
        transaction = {
            "merchant" : merchant,
            "category" : category,
            "amount" : float(amount)
        }

        total_spending += transaction["amount"]
        if largest_transaction < transaction["amount"]:
            largest_transaction = transaction["amount"]
            largest_merchant = transaction["merchant"]
        transactions.append(transaction)
    
    for transaction in transactions:
        if transaction["amount"] >= 50:
            transaction_equal_or_over_fifty.append(f"{transaction['merchant']} - ${transaction['amount']}")


    print(transactions)
    print(f"Total spending: ${total_spending}")
    print(f"Largest transaction: {largest_merchant} - ${largest_transaction}")

    print("Transactions >= 50:")
    for row in transaction_equal_or_over_fifty:
        print(row)