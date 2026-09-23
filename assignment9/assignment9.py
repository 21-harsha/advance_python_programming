
import csv
import json

input_file = "input1.csv"
output_file = "output1.json"

# Open and read CSV file
with open(input_file, "r") as file:
    data = csv.DictReader(file)
    records = list(data)

# Write data to JSON file
with open(output_file, "w") as file:
    json.dump(records, file, indent=4)

print("CSV data converted to JSON successfully.")