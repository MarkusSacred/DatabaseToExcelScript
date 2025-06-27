import os
import pandas as pd

# Origin and destination paths
source_path_folder = r"C:\Users\215MArcedas\Desktop\fileFolder"
destination_path_folder = r"C:\Users\215MArcedas\Desktop\destinationFolder"
file_name = "report.csv"

full_source_path = os.path.join(source_path_folder, file_name)
full_destination_path = os.path.join(destination_path_folder, "Converted.xlsx")

# Read the CSV file as lines, filter out lines containing "rows affected"
with open(full_source_path, 'r', encoding='latin1') as f:
    lines = f.readlines()

# Filter lines that do NOT contain "rows affected"
filtered_lines = [line for line in lines if "rows affected" not in line.lower()]

# Now read the filtered lines into a pandas DataFrame
from io import StringIO
filtered_csv = StringIO(''.join(filtered_lines))

# Make sure your headers list is correct (you missed a comma in your original script)
custom_headers = ['ID', 'Name', 'Age', 'Gender', 'City', 'BirthDate', 'Country']

df = pd.read_csv(filtered_csv, header=None, names=custom_headers, encoding='latin1')

# Save to Excel
df.to_excel(full_destination_path, index=False)

print(f"Converted CSV saved to {full_destination_path} without 'rows affected' lines.")
