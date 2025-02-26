# Your turn: Refactoring

## Objectives

1. Use the various refactorings to "fix" bad code

We are going to use a project located in the same folder as this file called `smelly_podcast` (as in code smells). This is code we used to download some things from Talk Python To Me.

It has been _contorted_ to have many problems or [code smells](https://en.wikipedia.org/wiki/Code_smell). We'll use refactoring to freshen this up.

**Note**: Before you first run this app, you'll need to make sure you have a virtual environment active and `requests` installed via pip.

## Large method *smell*

Look at `program.py` and notice this somewhat complex app is actually just one big method, yuck. We'll use several refactorings to fix this.

First, notice the section with the comment **"SHOW THE HEADER"**.

Take that small piece of code and make it its own method. Highlight the lines, choose **Refactor > Refactor this**.

Choose method and name it `show_header`. Notice it was created below and called from your current location.

After each refactoring, run the program to make sure it still works!

(It should :) ).

-----------------------

Next, make a method out of **"DOWNLOAD THE EPISODE DATA"**. Name it `download_data`. Be sure to leave `url` above in the original method and be sure to include the for-in loop as part of this method. This will show you how local data becomes parameters in the resulting method:

```python
url = 'https://talkpython.fm/episodes/rss'
download_data(url)
```

Now we have this `url` variable and then immediately use it once. Let's just pass the value directly to the method:

```python
download_data('https://talkpython.fm/episodes/rss')
```

Accomplish this by refactoring the `url` variable and choosing *inline variable*.


-----------------------


Next up, we have the **"GET SHOW ID RANGE"** section. We want a method that will return both the `latest_show_id` as well as the `oldest_show_id`. This is interesting because you'll see that PyCharm knows about tuple packing/unpacking on method calls. Highlight both:

```python
latest_show_id = max(episode_data.keys())
oldest_show_id = min(episode_data.keys())
```

And extract them into a single method: 

```python
latest_show_id, oldest_show_id = get_show_id_range()
```

-----------------------


Now find the single line annotated with **"GET EPISODE"**. Highlight only this in the line: `episode_data.get(show_id)` and refactor it to a method called `get_episode`.

-----------------------

Finally, notice the remaining section label **"DISPLAY RESULTS"**.

Highlight that and extract it to `display_results(latest_show_id, oldest_show_id)`.

Rerun your program (again). It's still working right? OK then, carry on.

## Large module *smell*

Our code is MUCH better already. But let's separate the usage of this functionality from its implementation. We'll move the parts to do with downloading and parsing episodes to `service.py`.

Let's move the data container and type first. Highlight these two lines and "move" them via refactoring to `service.py`.

	Episode = namedtuple('Episode', 'title link pubdate show_id')
	episode_data = {}  

**Note**: If you have **not** opened just the `smelly_podcast` folder as the project root, you will need to market the folder `smelly_podcast` as a **sources root** for that to work. It should be **blue** like this:

![](./sources-root.png)

Open `service.py` and see that the lines have moved. Does your code still run?


-----------------------


We need to move some more of the methods. Namely, move these all to service. Before you do it one by one, observe that you can move multiple things at once. Highlight one to move, choose move, and check the others off before agreeing to move them to `service.py`.

* `get_episode`
* `get_show_id_range`
* `download_data`

Now that is slick, right? Does your code still run? Good.


-----------------------


One final bit of clean up and code clarity: `import module` (rather than `from module import symbol`).

If you now look at the top of the `program.py` file, you'll see some existing imports are unused as well as it's generally messier.

```python
from service import Episode, episode_data, get_episode, get_show_id_range, download_data
```

We can do double-duty for clean up here. It would be nice if we saw where these methods came from in our code usages (think Zen of Python -> *Namespaces are one honking great idea -- let's do more of those!*). Put the cursor on one of the colored, not dimmed, symbols and choose "Covert to import service".

See how that import is cleaned up and our usage is more clear with the namespace? For example, it's clear `download_data` and `get_show_id_range` come from the `service` module now:

```python
def main():
    show_header()
    service.download_data('https://talkpython.fm/episodes/rss')
    latest_show_id, oldest_show_id = service.get_show_id_range()
    display_results(latest_show_id, oldest_show_id)
```


## Variable absence *smell*

**Variable absence** is a smell I created. There doesn't seem to be an agreed upon smell for it, but I'm sure you've seen it. Here's the deal. What does this mean:

`result = 7 * max(inputs) * (match / count)`

Let's try this one instead.

```python
largest_cell = max(inputs)
ratio = (match / count)
DICE_MULTIPLIER = 7

result = DICE_MULTIPLIER * largest_cell * ratio
```

Well, you'll still have to use your imagination. But it seems to do with a board game, rolling dice, etc. Why is one clear and the other isn't? The expression is computing many values inline all at the same time. Once named, the pieces are much clearer.

Open `service.py`. Notice this line `dom.findall('channel/item')` appears multiple times. It represents the `items` elements from the RSS feed (part of the RSS 2.0 spec). 

Make a variable for it by highlighting either single expression, choose refactor > variable. Name it something like `items`. Choose 2 locations!

Does your code still run? Then you're done. :)

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/mastering-pycharm-course/issues) or fix it and [submit a PR](https://github.com/talkpython/mastering-pycharm-course/pulls).*