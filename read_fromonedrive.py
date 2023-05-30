import win32com.client as win32
import pandas as pd

# Constants
onedrive_url = "<onedrive_url>"
file_path = "<file_path>"

# Create an instance of Excel
excel = win32.Dispatch("Excel.Application")

# Open the Excel file from OneDrive
workbook = excel.Workbooks.Open(f"https://{onedrive_url}/{file_path}")

# Read the Excel file into a DataFrame
sheet = workbook.Worksheets(1)
data_range = sheet.UsedRange
data = data_range.Value
header = data[0]
values = data[1:]

df = pd.DataFrame(values, columns=header)

# Print the data or perform other operations
print(df.head())

# Close the Excel file
workbook.Close()

# Quit Excel
excel.Quit()
