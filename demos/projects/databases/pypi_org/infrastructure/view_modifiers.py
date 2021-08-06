from functools import wraps

import flask
import werkzeug
import werkzeug.wrappers


def response(*, mimetype: str = None, template_file: str = None):
    def response_inner(f):
        # print("Wrapping in response {}".format(f.__name__), flush=True)

        @wraps(f)
        def view_method(*args, **kwargs):
            response_val = f(*args, **kwargs)

            if isinstance(response_val, werkzeug.wrappers.Response):
                return response_val

            if isinstance(response_val, flask.Response):
                return response_val

            if isinstance(response_val, dict):
                model = dict(response_val)
            else:
                model = dict()

            if template_file and not isinstance(response_val, dict):
                raise Exception(
                    "Invalid return type {}, we expected a dict as the return value.".format(type(response_val)))

            if template_file:
                response_val = flask.render_template(template_file, **response_val)

            resp = flask.make_response(response_val)
            resp.model = model
            if mimetype:
                resp.mimetype = mimetype

            return resp

        return view_method

    return response_inner

#
# def template(template_file: str = None):
#     def template_inner(f):
#         @wraps(f)
#         def view_method(*args, **kwargs):
#             data_dict = f(*args, **kwargs)
#             if not isinstance(data_dict, dict):
#                 raise Exception(
#                     "Invalid return type {}, we expected a dict as the return value.".format(type(data_dict)))
#
#             return flask.render_template(template_file, **data_dict)
#
#         return view_method
#
#     return template_inner
