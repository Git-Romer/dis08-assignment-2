# Welcome to our group repository

## General information

In this repository we will solve the Exercises from the second Assignment.
Furthermore all Links to every solution will be provided in this [README](./README.md) file.
Every exercise gets its own Folder in which you will find all the files containing the results. Whenever we can, we will work with the Jupyter Notebook. This will allow us to have our Python code and the corresponding Markdown explanation in one place and will therefore be much cleaner and simpler to read.

## Group information

* For better communication within the group there is a file called [tasklist.md](./tasklist.md) in which we will list all the To-do tasks to finish our job. So **before starting to work** check the [To-do list](./tasklist.md).

* Every group member has its own branch to use while working! This allows us to work simultaneously on the same document without breaking or losing our data.
  * **Usage:**
    * **Before starting to work**
      1. make sure to be in the `master` branch by typing: `git checkout master`.
      2. Update your local repository by typing: `git pull origin master`.
      3. Switch to your branch by typing: `git checkout [Yourbranchname]`.
      4. Now you need to update your own branch by typing: `git merge origin master`. **Warning** If you forgot to push your last work to your branch, the progress will be lost. In that case please make sure to do that before merging with master. To do so please refer to the last bulletpoint. As soon as everything is at its right place, you can start working.
    * **Before finishing work**
      1. save your files and add them to the stage by typing: `git add .`. This will add all your saved files to the stage. If you wish to stage only one file (for example to have different commit messages (*recommended*)) type this for each file: `git add "Yourfilename"` and commit it by typing: `git commit`. Repeat until all your files are committed.
      2. Push those changes to *your own* branch by typing: `git push origin [Yourbranchname]`. This will automatically create a pull request. It means that before merging the master branch with your own branch, this step will need to be approved by someone. This will allow you and others to see the changes and prevent messing up the master branch. Additionally this will prevent deleting progress if two persons are working on the same document.

## Links to Exercises

* [Exercise 0](./Exercise_0)
* [Exercise 1](./Exercise_1) &rarr; [Exercise_1.ipynb](./Exercise_1/Exercise_1.ipynb)
* [Exercise 2](./Exercise_2)

___

# Assignment 2

Second Assignment, Deadline: 2020-07-31, 23:59:59

In this assignment, you will work together in groups on a larger project that builds over several weeks.
The project will focus on getting data from the web, cleaning and writing data in Python.
The exercises will be posted in GitHub as usual.

## Rules

:heavy_check_mark: **Groups of 3 to 4**: You will work on this assignment in groups of 3 to 4 students each. Find your partners until 2020-06-04. Anyone not in a group by then will be assigned a random group by us.

:heavy_check_mark: **Be active**: As before, we want to see weekly commits from each of you in your repository. A last-minute commit for the assignment is suspicious...

:heavy_check_mark: **Everybody contributes equally**: You decide how to share the work in a group, but make sure that every member does roughly the same amount of work. If possible, make use of GitHub's collaboration features - e.g., one group member can be the designated "merge master" that receives pull requests and decides over code merges. Other modes of operation are possible, you decide - but we will eventually see in your commit log, who did what and when!

:heavy_check_mark: **Documentation, documentation, documentation**: Write a complementing `README.md` that explains your solutions, ideas, and so on. This will help the reviewers to understand what you did.

### :warning: If we get the feeling that you cheated, we will ask embarrassing questions and schedule a 1:1 interview! If you can’t explain your results in an 1:1 interview we will not accept your solutions and erase your points for this assignment

So... Play fair!
