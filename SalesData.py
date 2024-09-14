class SalesData:
    def __init__(self):
        self.saledata = []

    def add_transaction(self, customer_id, date, amount):
        saledata = {'customer_id': customer_id, 'date': date, 'amount': amount}
        self.saledata.append(saledata)
    
    def total_sales(self, customer_id):
        sum = 0
        for customer in self.saledata:
            cus = customer['customer_id']
            amo = customer['amount']
            if cus == customer_id:
                sum += amo
        return sum

    def top_customers(self, n):
        total_sales = []
        for customer in self.saledata:
            cus = customer['customer_id']
            lis = (cus, sales_data.total_sales(cus))
            total_sales.append(lis)
            total_sales.sort(key = lambda x:x[0])
        print(total_sales)


# Initialize the sales data
sales_data = SalesData()

# Add transactions
sales_data.add_transaction(1, "2024-01-10", 200.50)
sales_data.add_transaction(2, "2024-01-15", 150.75)
sales_data.add_transaction(1, "2024-02-01", 300.00)
sales_data.add_transaction(3, "2024-01-20", 450.25)

# Get total sales for a customer
print(sales_data.total_sales(1))  # Output: 500.50

# Get the top 2 customers by total sales
print(sales_data.top_customers(2))  # Output: [(3, 450.25), (1, 500.50)]