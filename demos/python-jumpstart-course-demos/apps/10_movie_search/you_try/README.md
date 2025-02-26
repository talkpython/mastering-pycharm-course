# App 10: Movie Search App

![image](app-10-screenshot.png)
 
Your turn. Try to build the interactive app above. 

This application use the Talk Python MovieDb API to search live movie data for movies 
matching the title in your search text. It focuses on being reliable 
even when the network fails or the user enters bad information.

Key concepts introduced
=================

**The API**

You can find the details of the JSON HTTP API at [movieservice.talkpython.fm](https://movieservice.talkpython.fm/).

**Try/Except Error Handling**

    try:
        method1()
        method2()
        method3()
    except ConnectionError as ce:
        # handle network error
    except Exception as x:
        # handle general error

**Raising your own errors and exceptions**

    class MovieClient:
        def __init__(self, search_text):

            if not search_text or not search_text.strip():
                raise ValueError('Must specify a search string.')

