# Solutions to Exercise 2

- Notebook:
  - [Exercise2.ipynb](./Exercise2.ipynb)
- CSV files:
  - Initial:
    - [lotr_clean.csv](./lotr_clean.csv)
  - Created by programs:
    - [movies.csv](./movies.csv)
- JSON files:
  - Initial:
    - [movies.json](./movies.json)
  - Created by programs:
    - [lotr_clean.csv_converted_to.json](./lotr_clean.csv_converted_to.json)
    - [lotr_converted.json](./lotr_converted.json)
- Programs:
  - [csv2json.py](./csv2json.py)

___

## Exercise 2

### Task 1

Write a Python program `csv2json` to convert a given CSV file into a JSON file. This conversion should be generic as possible and able to convert different types of CSV files. For the beginning try to make it work with the [`lotr_clean.csv`](lotr_clean.csv) file I uploaded to GitHub. Think about the generic parts. Where do the JSON key names come from? What about different types of separators? Try to build your program from "simple" to "a bit more complex" and think about how to split the development within your group. Document your program and remember to commit early and commit often.

### Task 2

Your task is to transform a dataset on movies since 1950. Download the dataset [`movies.json`](movies.json) from our Github repository. Write a Python program to:

1. read in the data from the JSON file,
2. count for each year, how many movies per genre have appeared,
3. create a CSV file where for each year, the counts for each genre are listed.

Your final CSV should look something like this:

year|Action|Adventure|Animation|...
-----|------|----------|--------|---
1950|39|42|65|...
1951|...|...|...|...

### Bonus

Create some interesting figures (in spreadsheet software, with R or any other visualitation software you know) on the development of genres over time.
