import os
import pandas as pd
class AddProudctsPage:
    def Fetchstocks(LocationName):
         Full_Path = os.path.join(os.getcwd(),"Database")
         FilePath = os.path.join(Full_Path,f"{LocationName}.xlsx")
         df = pd.read_excel(FilePath)
         stock_names=df.columns.to_list()
         stock_names.remove("ProductName")
         stock_names.remove("Quantity")
         return stock_names
    
    def addStocks(ProductName, Quantity, Stockroom, LocationName):
          Full_Path = os.path.join(os.getcwd(), "Database")
          FilePath = os.path.join(Full_Path, f"{LocationName}.xlsx")

          df_existing = pd.read_excel(FilePath)
          new_row = {"ProductName": ProductName, "Quantity": Quantity, Stockroom: "Y"}
          df_new_row = pd.DataFrame([new_row])  # Create a DataFrame for the new row
          df_updated = pd.concat([df_existing, df_new_row], ignore_index=True)

          with pd.ExcelWriter(FilePath, engine="openpyxl", mode='w') as writer:
               df_updated.to_excel(writer, index=False)
          
          return "Stock Added"
          

    
