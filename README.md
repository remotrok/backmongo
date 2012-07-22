# BackMongo

It's a simple REST interface for MongoDB written in Python that can be used straight away from a Backbone application.
It's an alpha version.
We are using it to develop backbone apps without having to worry about the server side. We've coded what we've needed so far. In the future we plan to add more features, such as, authentication, user privileges, etc.

At the moment backmongo can be only used as a flask extension, but we plan to add extensions from other frameworks.


## Requirements
* flask
* pymongo

You could install all with

    $ [sudo] pip install -r requirements.txt

## Use

### as a Flask extension

    from flask import Flask
    from flask.ext import backmongo

    app = Flask(__name__)
    backmongo.init_app(app)

    if __name__ == "__main__":
        app.run(debug=True)

### From the command line

    $ python flask_backmongo.py path/to/project/dir


## Examples
There's an example in examples/todos/ (a slightly modified version of [this][0]) that illustrates how easy it's to use backmongo from a backbone application.

## Tests
There are several integration tests coded in javascript using Mocha running on Node.
We wrote two posts about how to troubleshoot several problems we came across while setting the tests environment:

 - [Using Mocha to test a Backbone application on Node.js][1]
 - [Avoiding XMLHTTPRequest problem using jQuery on Node.js][2]

 To execute the tests you need to install Mocha globally

    $ npm install -g mocha

and later install the other required modules locally

    $ npm install should
    $ npm install jquery
    $ npm install backbone
    $ npm install xmlhttprequest

Then you have to type in the console

    $ make

this starts a flask app that use backmongo, execute the javascript tests with mocha and stop the flask app.

By default the tests are working in a data base called **backmongo**. If you need to change this create a file named **backmongo_conf.py** in the root folder, or in some place in your **PYTHONPATH**, and set the data base name in the variable **DATABASE**. You could see an configuration file example in **examples/todo/static/backmongo_conf.py**

[0]: http://backbonejs.org/#examples-todos
[1]: http://garajeando.blogspot.com.es/2012/04/using-mocha-to-test-backbone.html
[2]: http://garajeando.blogspot.com.es/2012/06/avoiding-xmlhttprequest-problem-using.html
[3]: http://visionmedia.github.com/mocha/
[4]: https://github.com/visionmedia/should.js







