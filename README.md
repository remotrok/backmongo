# BackMongo

It's a simple REST interface for MongoDB written in Python that can be used straight away from a Backbone application.
It's an alpha version. We are using **backmongo** to develop backbone apps without having to worry about the server side. We've coded just what we've needed so far. In the future we plan to add more features, such as, authentication, user privileges, etc.

At the moment **backmongo** can be only used as a flask extension, but we plan to add extensions for other frameworks.


## Requirements
* flask
* pymongo

You can install them all with:

    $ [sudo] pip install -r requirements.txt

## Use

### As a Flask extension:

    from flask import Flask
    from flask.ext import backmongo

    app = Flask(__name__)
    backmongo.init_app(app, url_prefix='API')

    if __name__ == "__main__":
        app.run(debug=True)

### From the command line:

    $ python flask_backmongo.py path/to/project/dir


## Examples
There's an example in **examples/todos/** (it's a slightly modified version of [the backbone's todo example][0]) that illustrates how easy it's to use **backmongo** from a backbone application.

## Tests
There are several integration tests coded in javascript using Mocha running on Node.
We wrote two posts about how to troubleshoot several problems we came across while setting the tests environment:

 - [Using Mocha to test a Backbone application on Node.js][1]
 - [Avoiding XMLHTTPRequest problem using jQuery on Node.js][2]

To execute the tests you need to install Mocha globally

    $ npm install -g mocha

and then install locally the other required modules.

    $ npm install should
    $ npm install jquery
    $ npm install backbone
    $ npm install xmlhttprequest

Then you have to type in the console:

    $ make

which starts a flask app using **backmongo**, executes the javascript tests with mocha and finally stops the flask app.

By default the tests are working in a data base called **backmongo**. If you need to change it, just create a file named **backmongo_conf.py** in the root folder, or in some other place in your **PYTHONPATH**, and set the data base name in the variable **DATABASE**. There is an example of configuration file in **examples/todo/static/backmongo_conf.py**

## Todo
* Prepare and submit BackMongo to the Python Package Index.

[0]: http://backbonejs.org/#examples-todos
[1]: http://garajeando.blogspot.com.es/2012/04/using-mocha-to-test-backbone.html
[2]: http://garajeando.blogspot.com.es/2012/06/avoiding-xmlhttprequest-problem-using.html
[3]: http://visionmedia.github.com/mocha/
[4]: https://github.com/visionmedia/should.js



