with open("./transactions.csv") as file:
    data = file.readlines()
    transactions = []

    # strip removes \n from the row
    # split separates values by provided delimiter
    for row in data[1:]:
        merchant, category, amount = row.strip().split(",")
        transaction = {
            "merchant" : merchant,
            "category" : category,
            "amount" : float(amount)
        }
        transactions.append(transaction)
    print(transactions)