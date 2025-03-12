# Your turn: HTTP Endpoint Testing

## Version warning

This chapter requires PyCharm Professional to complete as indicated. Please see the [version breakdown](https://www.jetbrains.com/pycharm/editions/) at JetBrains.

## Objectives

1. Test an existing web page using HTTP Client
2. Call an API using HTTP Client
3. Submit data to a password-protected API endpoint using JSON

## Create an HTTP client file

To get started, you're welcome to use an existing project or create a brand new one. A Virtual environment is not required this time.

Create a new HTTP Request file named `blog.http`. You'll see the *hello world* style placeholder from PyCharm. Go ahead and run it to see it's all hanging together. Then feel free to delete that section.

## Requesting a web page (with redirect)

We'll start by checking out what's at [talkpython.com](https://talkpython.com). If you load it in your browser, you'd see it does work. But we get more info if we use the HTTP Client. Put a GET request to pull `https://talkpython.com`. You'll get quite a bit of content back when you run it. 

Got to the top of the request output and see if you can find a 301 redirect response.

Notice there is a *disable* link / button near that request in the output. If you click it, it will modify the response to avoid following redirects for further exploration. Try that out as well. Expand the headers and check out the `location` value.

## Requesting all the blog entries

For our API, we are going to be working with [consumerservicesapi.talkpython.fm](https://consumerservicesapi.talkpython.fm). Give it a quick look to see what's there. 

First, we just want to see all the blog posts at the API. Add a request for `https://consumerservicesapi.talkpython.fm/api/blog`. Run this and see the output. Also, inspect the saved JSON file.

## Create a new blog post

Now we can use the **POST: /api/blog/** endpoint to create a new blog post. We'll need to submit data as JSON matching the following format:

```json
{
  "published": "2025-04-01",
  "view_count": 1234,
  "content": "BODY CONTENT",
  "title": "TITLE"
}
```

It's time to submit something pithy using HTTP Client. 

After you do, rerun get blog entries or use the **GET: /api/blog/{id}** endpoint to pull back that created entry to see that it was created successfully.

## Removing domain from endpoint spec

We can create a new run environment to avoid specifying the full domain `consumerservicesapi.talkpython.fm` from each request. This can be helpful in development and QA when building and testing the service at the same time.

1. Click the "Run with: ..." dropdown at the top of the UI
2. Choose "Add environment to private file"
3. Leave "dev" in place but add a variable `base_url` and set it to `https://consumerservicesapi.talkpython.fm`.
4. Exclude this file from git (or imagine that you would... :) )
5. Switch back to **blog.http** and select the new environment
6. Replace the url base with `{{base_url}}`
7. Ensure things still run.

*See a mistake in these instructions? Please [submit a new issue](https://github.com/talkpython/mastering-pycharm-course/issues) or fix it and [submit a PR](https://github.com/talkpython/mastering-pycharm-course/pulls).*
