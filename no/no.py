import pandas as pd

def categorize_data(file_path):
    df = pd.read_excel(file_path)

    categories = {}

    for index, row in df.iterrows():
        product_name = row['ProductName']
        quantity = row['Quantity']

        for col_name, value in row.items():
            if col_name != 'ProductName' and col_name != 'Quantity' and value == 'Y':
                if col_name not in categories:
                    categories[col_name] = {'ProductNames': []}
                categories[col_name]['ProductNames'].append(product_name)

    return categories

def find_stockroom(product_name, categories):
    for stockroom, items in categories.items():
        if product_name in items['ProductNames']:
            return stockroom
    return None

def group_products_by_stockroom(user_list, categories):
    stockroom_groups = {}

    for product_name in user_list:
        stockroom = find_stockroom(product_name, categories)
        if stockroom:
            if stockroom not in stockroom_groups:
                stockroom_groups[stockroom] = []
            stockroom_groups[stockroom].append(product_name)

    return stockroom_groups

def take_user_list():
    user_list = []
    print("Enter the list of product names (enter 'done' when finished):")
    while True:
        product_name = input("Product name: ").strip()
        if product_name.lower() == 'done':
            break
        user_list.append(product_name)
    return user_list



file_path = 'Database/Chick Fil A.xlsx'

user_list = take_user_list()

categories = categorize_data(file_path)

stockroom_groups = group_products_by_stockroom(user_list, categories)

for stockroom, products in stockroom_groups.items():
    print(f"Stockroom: {stockroom}")
    print("Products:", products)
    print()
