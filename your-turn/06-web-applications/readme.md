# Your turn: Web

## Version warning

This chapter requires PyCharm Professional to complete as indicated. Please see the [chart for version breakdown](https://training.talkpython.fm/courses/explore_pycharm/mastering-pycharm-ide#editions) in the public course page.

## Objectives

1. Create a basic Flask web app
2. Implement a view method
3. Render data from view in the template
4. Change the global site look and feel

## A basic Flask web app

We are going to use PyCharm's tools to create a Flask web app.

We'll let PyCharm create most of this for us at the start.

1. Open PyCharm
2. Choose "Create new project"
3. Pick Flask
4. Expand the "Project interpreter"
5. Verify you're using Python 3.8 or higher in a virtual environment.
4. Expand the "More settings" section.
5. Make sure the template language is `Jinja2`
6. Name your project and create it

Now that you have the project created, PyCharm will have already installed Flask and its dependencies in the virtual environment it created for you.  Moreover, it has configured Flask to run with the flask CLI commands rather than Python's native style (e.g. `flask run` rather than `python3 app.py`).

![Flask is ready to run](./resources/ready-to-run.png)

And you'll have the typical "hello world" Flask app:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
```

Go ahead and run the app by pressing the green arrow in the screenshot above. You should see something like this:

![First run](./resources/first-run.png)

## Implement a view method

Let's add a little structure. Create a top-level folder called `data`. In the `data` folder, create called `fake_data.py`. Copy this method into that file:

```python
def get_orders():
    return [
        {'name': 'Cereal', 'price': 4.99},
        {'name': 'Cheese', 'price': 2.15},
        {'name': 'Milk', 'price': 6.99},
        {'name': 'Oranges', 'price': 2.54},
        {'name': 'Apples', 'price': 1.99},
        {'name': 'Bread', 'price': 2.99},
    ]
```

Now let's use it in the website.

We're going to *replace* the `hello_world()` view method with one called `index()`. Traditionally, websites default file server has been `index.html` for urls such as `https://the_server.com/` so we'll mirror that in the Flask style.

Now, let's get the data from our simulated database (`fake_data.py`) into the view method. Import fake_data and use it to store the orders in a local variable:

```python
@app.route('/')
def index():
    orders = fake_data.get_orders()
    return 'Hello World!'
```

Go ahead and run the app again and request the home page just to make sure things are still hanging together.


## Render data in the template

Now you have the data ready to send along to the HTML side of things, let's create the Jinja template and render the orders there.

Create a new HTML file: `templates/index.html` (this should use PyCharm's HTML template with a little structure). Now it's time to use Jinja's syntax to render the orders. Just do something simple like this:

```html
<!-- ... -->
<h1>Flask Orders</h1>

{% for o in orders %}
    <div>
        <span style="font-weight: bold;">{{ o.name }}</span>
        <span>{{ o.price }}</span>
    </div>
{% endfor %}
<!-- ... -->
```

Do not copy / paste this. Type it in to see how PyCharm helps you with autocomplete and more.

Finally, we'll jump back to our `index()` view method and render the template with the order data:

```python
@app.route('/')
def index():
    orders = fake_data.get_orders()
    return flask.render_template('index.html', orders=orders)
```

With this code in place, you should have a nav icon to jump between the view method and template:

![Nav icon](./resources/nav-icon.png)

## The global site template

Finally, let's see how we go about working across the site. Create a new HTML file that will hold the outer "shell" of our site with a common set of imports, styles, and so on. Create `templates/_layout.html`. I like the `_` prefix to indicate it's not a public page but a shared item.

Add something like this in there. Note the `block` keyword to allow us to use this across other pages. Also, we threw in some styles just to make the effect of the template more obvious. In real apps, you'd put that in a style sheet, but we want to keep this simpler if possible for this walk-through.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask Orders</title>
</head>
<body style="margin: 0px; background-color: #222; ">

<div style="padding: 20px; background-color: white;">
    {% block main_content %}{% endblock %}
</div>

<footer style="color: #888; margin-top: 50px; text-align: center;">
    <div class="copyright">
        This is a demo site built during a course.<br>
        Copyright <em>me</em>!
    </div>
</footer>

</body>
</html>
```

Finally, update the `index.html` file to use this template. Note that this is the entire page contents:

```html
{% extends "_layout.html" %}
{% block main_content %}

<h1>Flask Orders</h1>

{% for o in orders %}
    <div>
        <span style="font-weight: bold;">{{ o.name }}</span>
        <span>{{ o.price }}</span>
    </div>
{% endfor %}

{% endblock %}
```

Be sure to run and inspect your new site! It should look somewhat like this.

![Finished version of the site](./resources/done.png)

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/mastering-pycharm-course/issues) or fix it and [submit a PR](https://github.com/talkpython/mastering-pycharm-course/pulls).*
