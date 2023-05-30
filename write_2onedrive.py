import win32com.client as win32

# Create an instance of Excel
excel = win32.Dispatch("Excel.Application")

# Open the Excel file
workbook = excel.Workbooks.Open(r"C:\path\to\your\file.xlsx")

# Save the Excel file to OneDrive
onedrive_path = r"https://<your_onedrive_url>/Documents/"
workbook.SaveAs(onedrive_path + "file.xlsx")

# Close the Excel file
workbook.Close()

# Quit Excel
excel.Quit()

print("Excel file saved to OneDrive successfully.")
