# Your turn: Databases

## Version warning

This chapter requires PyCharm Professional to complete as indicated. Please see the [chart for version breakdown](https://training.talkpython.fm/courses/explore_pycharm/mastering-pycharm-ide#editions) in the public course page.

## Objectives

1. Open an existing SQLite database in PyCharm
2. Run queries against existing data
3. View table diagrams
4. See the Python + SQL integration in action 

**Note**: We will be working with a project called `database_proj` (creative, I know!) in the same folder as this file. Primarily we only care about the `db/blue_yellow.sqlite` file. You can run this program if you wish, but you must install the requirements first. That is not required however.

## An existing SQLite database in PyCharm

Open the project called `database_proj` in the same folder as this file. You may want to create a virtual environment first.

First, you'll add the SQLite data file `db/blue_yellow.sqlite` as a data source in PyCharm. Try dragging that file onto the database tab (when expanded).

If that works, great! If not, hit the plus in that tab, choose data source, sqlite (xenial). If you see any message about downloading database drivers do that first. Then you should be able to add the data file.

Explore the data in this tab. Expand it, play with it, and so on. Feel free to add a new table or new index to an existing one. Do not change the schema if you want the program to run. ;)

## Queries against existing data

To run a query, let's find all tracks that have the word 'the' in the title. Right-click on a table and choose jump to console. Write the query in SQL with the help of auto complete. The key where clause here is: 

`name LIKE '%the%'`

There should be 5 tracks that match.

## View table diagrams

Understanding relational tables is often best done via diagrams. Select `Track` and `Album` and choose Diagram > Show visualization from the right-click menu.

## Python + SQL integration in action 

The final trick is for inline SQL in code. Type, do not paste, the following code into the bottom of `data_app.py` and watch how the string first becomes SQL aware then even aware of your schema.

```python
query = "SELECT * FROM Album WHERE has_preview AND year > 2001"
```

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/mastering-pycharm-course/issues) or fix it and [submit a PR](https://github.com/talkpython/mastering-pycharm-course/pulls).*