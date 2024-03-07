import pandas as pd
import os

def make_new_location():
    #This will be Used As File name
    LocationName = "Chick-Fil-A"

    #These are user input for stockroom names
    NameOfStockRoom = ["BigStockRoom","SmallStockRoom"]
    
    # These are PreDefine Static column Names
    DefaultColumns = ["ProductName","Quantity"]
    CustomColumns = DefaultColumns + NameOfStockRoom #merged two List

    #GetPath To Save Excel File

    Full_Path = os.path.join(os.getcwd(),"Database")

    df = pd.DataFrame(columns=CustomColumns)

    FilePath = os.path.join(Full_Path,f"{LocationName}.xlsx") # Get Final Path
    df.to_excel(FilePath,index=False,index_label="") #Save Excel File


make_new_location()