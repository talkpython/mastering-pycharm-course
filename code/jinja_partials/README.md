# Jinja Partials

Simple reuse of partial HTML page templates in the Jinja template language for Python web frameworks.
(There is also a [Pyramid/Chameleon version here](https://github.com/mikeckennedy/chameleon_partials).)

## Overview

When building real-world web apps with Flask + Jinja2, it's easy to end up with repeated HTML fragments.
Just like organizing code for reuse, it would be ideal to reuse smaller sections of HTML template code.
That's what this library is all about.

## Example

This project comes with a sample flask application (see the `example` folder). This app displays videos
that can be played on YouTube. The image, subtitle of author and view count are reused throughout the
app. Here's a visual:

![](https://raw.githubusercontent.com/mikeckennedy/jinja_partials/main/readme_resources/reused-html-visual.png)

Check out the [**demo / example application**](https://github.com/mikeckennedy/jinja_partials/tree/main/example) 
to see it in action. 

## Installation

It's just `pip install jinja-partials` and you're all set with this pure Python package.

## Usage

Using the library is incredible easy. The first step is to register the partial method with Jinja and Flask.
Do this once at app startup:

```python
import flask
import jinja_partials

app = flask.Flask(__name__)

jinja_partials.register_extensions(app)
# ...
```

You can also use this library in your FastAPI (or Starlette) project!
```python
from fastapi.templating import Jinja2Templates
# or `from starlette.templating import Jinja2Templates`

import jinja_partials

templates = Jinja2Templates("tests/test_templates")

jinja_partials.register_starlette_extensions(templates)
# ...
```

Or directly using a jijna environment!
```python
import jinja_partials
from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("tests/test_templates"))
jinja_partials.register_environment(environment)
# ...
```

Next, you define your main HTML (Jinja2) templates as usual. Then 
define your partial templates. I recommend locating and naming them accordingly:

```
├── templates
│   ├── home
│   │   ├── index.html
│   │   └── listing.html
│   └── shared
│       ├── _layout.html
│       └── partials
│           ├── video_image.html
│           └── video_square.html
```

Notice the `partials` subfolder in the `templates/shared` folder.

The templates are just HTML fragments. Here is a stand-alone one for the YouTube thumbnail from
the example app:

```html
<img src="https://img.youtube.com/vi/{{ video.id }}/maxresdefault.jpg"
     class="img img-responsive {{ ' '.join(classes) }}"
     alt="{{ video.title }}"
     title="{{ video.title }}">
```

Notice that an object called `video` and list of classes are passed in as the model.

Templates can also be nested. Here is the whole single video fragment with the image as well as other info
linking out to YouTube:

```html
<div>
    <a href="https://www.youtube.com/watch?v={{ video.id }}" target="_blank">
        {{ render_partial('shared/partials/video_image.html', video=video) }}
    </a>
    <a href="https://www.youtube.com/watch?v={{ video.id }}" target="_blank"
       class="author">{{ video.author }}</a>
    <div class="views">{{ "{:,}".format(video.views) }} views</div>
</div>
```

Now you see the `render_partial()` method. It takes the subpath into the templates folder and
any model data passed in as keyword arguments.

We can finally generate the list of video blocks as follows:

```html
{% for v in videos %}

    <div class="col-md-3 video">
        {{ render_partial('shared/partials/video_square.html', video=v) }}
    </div>

{% endfor %}
```

This time, we reframe each item in the list from the outer template (called `v`) as the `video` model
in the inner HTML section.


## Why not just use `include` or `macro` from Jinja?

The short answer is they are nearly the same, but both fall short in different ways. 
For a more detailed response, see the discussion on [**issue #1**](https://github.com/mikeckennedy/jinja_partials/issues/1)