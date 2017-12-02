from pyramid.view import view_config


@view_config(route_name='home', renderer="templates/mytemplate.pt")
def my_view(_):
    return {
        'project': 'Demo project from PyCharm!',
        'data': [1, 1, 2, 3, 5, 8, 13, 21],
        'show_odds': True
    }
