#Simple python program for the code check with breakpoint analysis.
import pandas as pd
file_path = "C:/Users/Shrinivas/OneDrive/Desktop/data.xlsx"
# To read a specific sheet
df = pd.read_excel(file_path, sheet_name="Sheet1")
print(df.head())
