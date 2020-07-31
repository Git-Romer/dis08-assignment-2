# Solution to Exercise 3

- Notebook
  - [Exercise_3.ipynb](./Exercise_3.ipynb)
- CSV files
  - [List_of_countries_with_alcohol_prohibition.csv](./List_of_countries_with_alcohol_prohibition.csv)
- JSON files
  - [List_of_countries_with_alcohol_prohibition.json](./List_of_countries_with_alcohol_prohibition.json)

___

## Exercise 3  

In this final assignment, we would like you to develop a little web scraping project. This is the last part of the second assignment for this semester. It includes a lot of the different tools and steps you learned during this semester.

1. Pick a list within the Wikipedia like the [list of sovereign states](https://en.wikipedia.org/wiki/List_of_sovereign_states). Choose some other list on your own, based on your personal interests. The only requirement is that there are other Wikipedia articles linked within the list.
2. Get all the names and URLs to the corresponding items in the list and export them into a CSV file that has two columns (name and URL).
3. For every Wikipedia article in the CSV list choose a few attributes from the infobox on the right that you would like to extract (e.g., population, name of the head of state, whatever...). Extract this information for every entry in your list. Store this information in an appropriate data structure.
4. Save your scraped information into a JSON file. Try to export *clean* data.
5. Document your program and development process. Tell us something about the data you scraped. Why did you choose this data? Can you think of a good use case for this data? As always: Push everything into your GitHub repository.

### Some hints

* Try to be kind to Wikipedia and yourself. You will most likely generate a lot of web traffic while scraping the same webpage again and again. This stresses the Wikipedia's server and takes a lot of time. Try to use a caching method like the one from [requests-cache](https://pypi.org/project/requests-cache/). Alternatively, you can download the HTML content using your script and then work locally.
* Try not to solve the whole problem at once. Remember the tactics desribed in the earlier lectures: [Divide and conquer](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm) - Step by step.
* Have a look at the two sample projects from [chapter 11](https://automatetheboringstuff.com/chapter11/). They do something similar.
* A lot of code examples for Beautiful Soup are documented in the [official documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).