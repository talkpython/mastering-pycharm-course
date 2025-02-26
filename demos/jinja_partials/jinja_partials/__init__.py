"""
jinja_partials - Simple reuse of partial HTML page templates in the Jinja template language for Python web frameworks.
"""

__version__ = '0.2.1'
__author__ = 'Michael Kennedy <michael@talkpython.fm>'
__all__ = [
    'register_extensions',
    'register_starlette_extensions',
    'register_environment',
    'render_partial',
    'generate_render_partial',
    'PartialsException',
]

from functools import partial
from typing import TYPE_CHECKING, Any, Callable, Optional, Union

from jinja2 import Environment
from markupsafe import Markup as Markup

try:
    import flask
except ImportError:
    flask = None

try:
    import starlette
except ImportError:
    starlette = None

if TYPE_CHECKING and flask and starlette:
    from flask import Flask
    from starlette.templating import Jinja2Templates


class PartialsException(Exception):
    pass


def render_partial(
        template_name: str,
        renderer: Optional[Callable[..., Any]] = None,
        markup: bool = True,
        **data: Any,
) -> Union[Markup, str]:
    if renderer is None:
        if flask is None:
            raise PartialsException('No renderer specified')
        else:
            renderer = flask.render_template

    if markup:
        return Markup(renderer(template_name, **data))

    return renderer(template_name, **data)


def generate_render_partial(renderer: Callable[..., Any], markup: bool = True) -> Callable[..., Markup]:
    return partial(render_partial, renderer=renderer, markup=markup)


def register_extensions(app: 'Flask'):
    if flask is None:
        raise PartialsException('Install Flask to use `register_extensions`')

    app.jinja_env.globals.update(render_partial=generate_render_partial(flask.render_template))


def register_starlette_extensions(templates: 'Jinja2Templates'):
    if starlette is None:
        raise PartialsException('Install Starlette to use `register_starlette_extensions`')

    def renderer(template_name: str, **data: Any) -> str:
        return templates.get_template(template_name).render(**data)

    templates.env.globals.update(render_partial=generate_render_partial(renderer))


def register_environment(env: Environment, markup: bool = False):
    def renderer(template_name: str, **data: Any) -> str:
        return env.get_template(template_name).render(**data)

    env.globals.update(render_partial=generate_render_partial(renderer, markup=markup))
