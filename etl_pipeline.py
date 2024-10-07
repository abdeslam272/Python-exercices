import pandas as pd

# Step 1: Extract - Load CSV into pandas DataFrame
Superstore = pd.read_csv('https://raw.githubusercontent.com/abdeslam272/Python-exercices/main/Superstore.csv', encoding='ISO-8859-1')
# print(Superstore.sample(10))

# To view column names and their types
print(Superstore.dtypes)

# # To get just the column names
# print(Superstore.columns)

# print(Superstore.shape) # 9994 lignes, 21 colonnes (9994, 21)

# # Index(['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode',
# #        'Customer ID', 'Customer Name', 'Segment', 'Country', 'City', 'State',
# #        'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category',
# #        'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit'],
# #       dtype='object')

# # Step 2: Transform - Clean and process data
# #some tests to see the state of data
# #Missing Data Checks (Null or NaN Values)
# print(Superstore['Order ID'].isnull().sum())
# print(Superstore['Order Date'].isnull().sum())
# print(Superstore['Ship Date'].isnull().sum())
# print(Superstore['Ship Mode'].isnull().sum())
# print(Superstore['Customer ID'].isnull().sum())
# print(Superstore['Customer Name'].isnull().sum())
# print(Superstore['Segment'].isnull().sum())
# print(Superstore['Country'].isnull().sum())
# print(Superstore['City'].isnull().sum())
# print(Superstore['Postal Code'].isnull().sum())
# print(Superstore['Region'].isnull().sum())
# print(Superstore['Product ID'].isnull().sum())
# print(Superstore['Category'].isnull().sum())
# print(Superstore['Sub-Category'].isnull().sum())
# print(Superstore['Product Name'].isnull().sum())
# print(Superstore['Sales'].isnull().sum())
# print(Superstore['Quantity'].isnull().sum())
# print(Superstore['Discount'].isnull().sum())
# print(Superstore['Profit'].isnull().sum())

# ##Everything is 0 so there's no missing data perfect

# #Duplicate Records Check
# print(Superstore.duplicated().sum())  # Total number of duplicate rows
# print(Superstore[Superstore.duplicated()])  # Display duplicate rows

# ##Everything is 0 so there's no duplicate records check

# #Range or Boundary Tests 
# ## we do this on Sales Quantity, Discount, Profit
# print(Superstore['Sales'].describe())
# print(Superstore['Quantity'].describe())
# print(Superstore['Discount'].describe())
# print(Superstore['Profit'].describe())

# ##everything seems logicals


# #Consistency Checks
# ##logically Order Date < Ship Date
# # Convert 'Order Date' and 'Ship Date' to datetime format
Superstore['Order Date'] = pd.to_datetime(Superstore['Order Date'], errors='coerce')
Superstore['Ship Date'] = pd.to_datetime(Superstore['Ship Date'], errors='coerce')

# To view column names and their types
print(Superstore.dtypes)

# # Check for rows where 'Order Date' is greater than or equal to 'Ship Date'
# inconsistent_dates = Superstore[Superstore['Order Date'] >= Superstore['Ship Date']]

# # Print the inconsistent rows
# print(inconsistent_dates)
