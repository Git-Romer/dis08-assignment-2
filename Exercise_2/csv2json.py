# Importing modules
import json
import os
import csv
print("Importing files...")
# Iterating over all files that end with ".csv" in the current working directory
for csvFilename in os.listdir("."):
    if not csvFilename.endswith(".csv"):
        continue
    print("Working...")
    # Opening the CSV file
    with open(csvFilename, "r") as csvFile:
        # Reading in a sample and testing which delimiter is used
        dialect = csv.Sniffer().sniff(csvFile.read(1000), delimiters=";,")
        csvFile.seek(0)
        # Reading in the CSV file
        reader = csv.DictReader(csvFile, delimiter = dialect.delimiter)
        # Searching for column headings
        column_names = reader.fieldnames
        # Creating base for later writing
        base = []
        for row in reader:
            base.extend([{column_names[i]:row[column_names[i]] for i in range(len(column_names))}])
        # Creating a new file
        with open(csvFilename + "_converted_to.json", "w") as jsonFile:
            # Writing data to the JSON file
            json.dump(base, jsonFile, indent=4)
print("Done!")
input("Press any key to continue.")