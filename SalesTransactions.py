class SalesTransactions:
    def __init__(self,transactions):
        self.transactions = transactions
    
    def total_spend_per_customer(self):
        my_dict = {}
        for i in range(len(transactions)):
            transaction = transactions[i]
            cus = transaction['customer_id']
            prix = transaction['price']
            if cus not in my_dict:
                my_dict[cus] = []
            my_dict[cus].append(prix)
            for cus in my_dict:
                
        return my_dict

            



transactions = [
    {'transaction_id': 1001, 'customer_id': 1, 'category': 'Electronics', 'price': 200.50, 'date': '2023-05-10', 'location': 'New York', 'payment_method': 'Credit Card'},
    {'transaction_id': 1002, 'customer_id': 2, 'category': 'Clothing', 'price': 150.75, 'date': '2023-06-15', 'location': 'Los Angeles', 'payment_method': 'Cash'},
    {'transaction_id': 1003, 'customer_id': 1, 'category': 'Electronics', 'price': 300.00, 'date': '2023-06-01', 'location': 'New York', 'payment_method': 'Credit Card'},
    {'transaction_id': 1004, 'customer_id': 3, 'category': 'Groceries', 'price': 45.25, 'date': '2023-05-20', 'location': 'Chicago', 'payment_method': 'Debit Card'},
    {'transaction_id': 1005, 'customer_id': 2, 'category': 'Clothing', 'price': 99.99, 'date': '2023-06-18', 'location': 'Los Angeles', 'payment_method': 'Cash'},
    {'transaction_id': 1006, 'customer_id': 1, 'category': 'Groceries', 'price': 50.75, 'date': '2023-05-11', 'location': 'New York', 'payment_method': 'Credit Card'},
    {'transaction_id': 1007, 'customer_id': 3, 'category': 'Electronics', 'price': 400.00, 'date': '2023-07-01', 'location': 'Chicago', 'payment_method': 'Credit Card'},
    {'transaction_id': 1008, 'customer_id': 4, 'category': 'Electronics', 'price': 600.75, 'date': '2023-07-10', 'location': 'San Francisco', 'payment_method': 'Credit Card'},
    {'transaction_id': 1009, 'customer_id': 5, 'category': 'Groceries', 'price': 80.25, 'date': '2023-07-11', 'location': 'New York', 'payment_method': 'Cash'},
    {'transaction_id': 1010, 'customer_id': 1, 'category': 'Clothing', 'price': 120.00, 'date': '2023-07-15', 'location': 'New York', 'payment_method': 'Debit Card'},
    {'transaction_id': 1011, 'customer_id': 5, 'category': 'Groceries', 'price': 35.99, 'date': '2023-07-20', 'location': 'New York', 'payment_method': 'Cash'},
    {'transaction_id': 1012, 'customer_id': 2, 'category': 'Groceries', 'price': 75.50, 'date': '2023-08-01', 'location': 'Los Angeles', 'payment_method': 'Credit Card'},
    {'transaction_id': 1013, 'customer_id': 3, 'category': 'Clothing', 'price': 250.25, 'date': '2023-08-10', 'location': 'Chicago', 'payment_method': 'Debit Card'},
    {'transaction_id': 1014, 'customer_id': 4, 'category': 'Electronics', 'price': 500.00, 'date': '2023-08-15', 'location': 'San Francisco', 'payment_method': 'Credit Card'},
    {'transaction_id': 1015, 'customer_id': 1, 'category': 'Electronics', 'price': 700.50, 'date': '2023-08-20', 'location': 'New York', 'payment_method': 'Credit Card'},
    {'transaction_id': 1016, 'customer_id': 2, 'category': 'Groceries', 'price': 100.00, 'date': '2023-08-25', 'location': 'Los Angeles', 'payment_method': 'Cash'}
]


sales = SalesTransactions(transactions)

# Example usage:
print(sales.total_spend_per_customer())  # Task 1