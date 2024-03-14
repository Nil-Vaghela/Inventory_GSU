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
                    categories[col_name] = {'ProductName': [], 'Quantity': []}
                categories[col_name]['ProductName'].append(product_name)
                categories[col_name]['Quantity'].append(quantity)

    return categories

file_path = 'Database/Chick Fil A.xlsx'

categories = categorize_data(file_path)

for stockroom, items in categories.items():
    print(f"Stockroom: {stockroom}")
    df_stockroom = pd.DataFrame(items)
    print(df_stockroom)
    print()
