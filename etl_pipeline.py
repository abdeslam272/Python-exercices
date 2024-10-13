import pandas as pd

# Step 1: Extract - Load CSV into pandas DataFrame
Superstore = pd.read_csv('https://raw.githubusercontent.com/abdeslam272/Python-exercices/main/Superstore.csv', encoding='ISO-8859-1')
# print(Superstore.sample(10))

# To view column names and their types
print(Superstore.dtypes)

# To get just the column names
print(Superstore.columns)

print(Superstore.shape) # 9994 lignes, 21 colonnes (9994, 21)

# Index(['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode',
#        'Customer ID', 'Customer Name', 'Segment', 'Country', 'City', 'State',
#        'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category',
#        'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit'],
#       dtype='object')

# Step 2: Transform - Clean and process data
#some tests to see the state of data
#Missing Data Checks (Null or NaN Values)
print(Superstore['Order ID'].isnull().sum())
print(Superstore['Order Date'].isnull().sum())
print(Superstore['Ship Date'].isnull().sum())
print(Superstore['Ship Mode'].isnull().sum())
print(Superstore['Customer ID'].isnull().sum())
print(Superstore['Customer Name'].isnull().sum())
print(Superstore['Segment'].isnull().sum())
print(Superstore['Country'].isnull().sum())
print(Superstore['City'].isnull().sum())
print(Superstore['Postal Code'].isnull().sum())
print(Superstore['Region'].isnull().sum())
print(Superstore['Product ID'].isnull().sum())
print(Superstore['Category'].isnull().sum())
print(Superstore['Sub-Category'].isnull().sum())
print(Superstore['Product Name'].isnull().sum())
print(Superstore['Sales'].isnull().sum())
print(Superstore['Quantity'].isnull().sum())
print(Superstore['Discount'].isnull().sum())
print(Superstore['Profit'].isnull().sum())

##Everything is 0 so there's no missing data perfect

#Duplicate Records Check
print(Superstore.duplicated().sum())  # Total number of duplicate rows
print(Superstore[Superstore.duplicated()])  # Display duplicate rows

##Everything is 0 so there's no duplicate records check

#Range or Boundary Tests 
## we do this on Sales Quantity, Discount, Profit
print(Superstore['Sales'].describe())
print(Superstore['Quantity'].describe())
print(Superstore['Discount'].describe())
print(Superstore['Profit'].describe())

#everything seems logicals


#Consistency Checks
##logically Order Date <= Ship Date
# Convert 'Order Date' and 'Ship Date' to datetime format
Superstore['Order Date'] = pd.to_datetime(Superstore['Order Date'], errors='coerce')
Superstore['Ship Date'] = pd.to_datetime(Superstore['Ship Date'], errors='coerce')

# # To view column names and their types
# print(Superstore.dtypes)

# Check for rows where 'Order Date' is greater than or equal to 'Ship Date'
inconsistent_dates = Superstore[Superstore['Order Date'] > Superstore['Ship Date']]

# Print the inconsistent rows
print(inconsistent_dates)

## so far there's no record where the order date is bigger than then the ship date: perfect

# Uniqueness Check
print(Superstore['Order ID'].nunique())  # 5009 => logique a person can do more than order
print(Superstore['Row ID'].nunique()) #9994 
print(Superstore['Customer ID'].nunique()) #793 => we can have more customers that doing more than an order

## Find orders with duplicate 'Order ID'
duplicate_orders = Superstore[Superstore.duplicated(subset=['Order ID'], keep=False)]

## Sort by 'Order ID' for better readability
duplicate_orders_sorted = duplicate_orders.sort_values('Order ID')

## Display the first few rows to see examples
print(duplicate_orders_sorted.head(10))


# Data Type Validation
## Change 'Postal Code' to object (string)
Superstore['Postal Code'] = Superstore['Postal Code'].astype(str)
print(Superstore.dtypes)  # Check the data types of each column

## we make it the enough changes
# Cardinality Checks
## Check cardinality of key columns
print("Order ID Cardinality:", Superstore['Order ID'].nunique())  # High cardinality expected
print("Row ID Cardinality:", Superstore['Row ID'].nunique())      # High cardinality expected
print("Customer ID Cardinality:", Superstore['Customer ID'].nunique())  # Medium-High cardinality
print("Product ID Cardinality:", Superstore['Product ID'].nunique())    # High cardinality
print("Ship Mode Cardinality:", Superstore['Ship Mode'].nunique())      # Low cardinality expected
print("Segment Cardinality:", Superstore['Segment'].nunique())          # Low cardinality expected
print("Category Cardinality:", Superstore['Category'].nunique())        # Low cardinality expected
print("Postal Code Cardinality:", Superstore['Postal Code'].nunique())  # Medium cardinality expected

# Referential Integrity (Foreign Key Checks)
## I have just one table

# Outliers Detection
###################

# Date Range Validation
print(Superstore['Order Date'].min(), Superstore['Order Date'].max())
print(Superstore['Ship Date'].min(), Superstore['Ship Date'].max())

## Calculate the difference between Ship Date and Order Date
Superstore['Days_Difference'] = (Superstore['Ship Date'] - Superstore['Order Date']).dt.days

## Check for orders where the shipping took more than 365 days (1 year)
long_shipping_times = Superstore[Superstore['Days_Difference'] > 365]
print(long_shipping_times)

# Integrity Checks for Calculated Fields
## Profit=(Sales×(1−Discount))−Cost
## Expected Profit=Sales×Discount
## Calculate the expected profit based on sales and discount
Superstore['Expected Profit'] = Superstore['Sales'] * Superstore['Discount']

## Check for rows where there are significant differences between Expected Profit and actual Profit
profit_discrepancy = Superstore[abs(Superstore['Profit'] - Superstore['Expected Profit']) > 0.01]  # tolerance for small differences
print(profit_discrepancy)

# Missing Categories or Unexpected Values
## 
## Define expected categories for Ship Mode
expected_ship_modes = ['Standard Class', 'Second Class', 'First Class', 'Same Day']

## Get unique values in the 'Ship Mode' column
unique_ship_modes = Superstore['Ship Mode'].unique()

## Find unexpected categories
unexpected_ship_modes = set(unique_ship_modes) - set(expected_ship_modes)
print("Unexpected Ship Modes:", unexpected_ship_modes)


## Define expected segments
expected_segments = ['Consumer', 'Corporate', 'Home Office']

## Get unique values in 'Segment' column
unique_segments = Superstore['Segment'].unique()

## Find unexpected categories
unexpected_segments = set(unique_segments) - set(expected_segments)
print("Unexpected Segments:", unexpected_segments)

## Transform Part

# Adding a 'Shipping Duration' column
Superstore['Shipping Duration'] = (Superstore['Ship Date'] - Superstore['Order Date']).dt.days

# Extracting year and month from the 'Order Date'
Superstore['Order Year'] = Superstore['Order Date'].dt.year
Superstore['Order Month'] = Superstore['Order Date'].dt.month

print(Superstore.dtypes)

# To get just the column names
print(Superstore.columns)

## Loading Part
# let's create our dim_customer.sqlite
import sqlite3
# Establish SQLite connections
conn = sqlite3.connect('abdeslam272/Python-exercices/dim_customer.sqlite')
cursor = conn.cursor()

# Create dim_customers table
cursor.execute('''
CREATE TABLE IF NOT EXISTS dim_customers (
    Customer_ID TEXT PRIMARY KEY,
    Customer_Name TEXT,
    Segment TEXT,
    Country TEXT,
    City TEXT,
    State TEXT,
    Postal_Code TEXT,
    Region TEXT
)
''')