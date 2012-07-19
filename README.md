# BackMongo

## Description
It's a simple REST interface for MongoDB written in Python that can be used straight away from a Backbone application.
It's an alpha version.
We are using it to develop backbone apps without having to worry about the server side. We've coded what we've needed so far. In the future we plan to add more features, such as, authentication, user privileges, etc.

At the moment backmongo can be only used as a flask extension, but we plan to add extensions from other frameworks.


## Requirements
* flask
* pymongo

## Use

### as a Flask extension

    from flask import Flask
    from flask.ext import backmongo

    app = Flask(__name__)
    backmongo.init_app(app)

    if __name__ == "__main__":
        app.run(debug=True)

### From de command line

    $ backmongo path/to/project/dir


## Examples
There's an example in examples/todos/ (a slightly modified version of [this][0]) that illustrates how easy it's to use backmongo from a backbone application.

## Tests
There are several integration tests coded in javascript using Mocha running on Node.
We wrote two posts about how to troubleshoot several problems we came across while setting the tests environment:

 - [Using Mocha to test a Backbone application on Node.js][1]
 - [Avoiding XMLHTTPRequest problem using jQuery on Node.js][2]

 To execute the tests you need to install first bla, bla.

 Then you have to start a flask server by executing:
 bla, bla from bla, bla directory
 Finally, the tests are run executing a make file:
 bla, bla  from bla, bla directory

[0]: http://backbonejs.org/#examples-todos
[1]: http://garajeando.blogspot.com.es/2012/04/using-mocha-to-test-backbone.html
[2]: http://garajeando.blogspot.com.es/2012/06/avoiding-xmlhttprequest-problem-using.html







