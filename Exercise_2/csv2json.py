# Importing modules
import json
import os
import csv
print("Importing files...")
for csvFilename in os.listdir("."):
    if not csvFilename.endswith(".csv"):
        continue
    print("Working...")
    with open(csvFilename, "r") as csvFile:
        dialect = csv.Sniffer().sniff(csvFile.read(1000), delimiters=";,")
        csvFile.seek(0)
        reader = csv.DictReader(csvFile, delimiter = dialect.delimiter)
        # Searching for column headings
        column_names = reader.fieldnames
        # Creating base for file
        base = []
        for row in reader:
            base.extend([{column_names[i]:row[column_names[i]] for i in range(len(column_names))}])
        # Writing data to the json file
        with open(csvFilename + "_converted_to.json", "w") as jsonFile:
            json.dump(base, jsonFile, indent=4)
print("Done!")
input("Press any key to continue.")