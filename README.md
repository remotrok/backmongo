## BackMongo

###Description
It's a simple MongoDB REST service written in Python that can be used straight away from a Backbone application.
It's an alpha version.
We are using it to develop backbone apps without having to worry about the server side. We've coded what we've needed so far. In the future we plan to add more features, such as, authentication, user privileges, etc.
At the moment backmongo can be only used as a flask extension, but we plan to add extensions from other frameworks.

###Requirements
flask, pymongo

###Examples
There's an example in examples/todos/ (a slightly modified version of this todo example __link__) that illustrates how easy it's to use backmongo from a backbone application.

###Tests
There are several integration tests coded in javascript using Mocha running on Node.
We wrote to posts about how to troubleshoot several problems we came across while setting the tests environment:
 - link 1
 - link 2

 To execute the tests you need to install first bla, bla.

 Then you have to start a flask server by executing:
 bla, bla from bla, bla directory
 Finally, the tests are run executing a make file:
 bla, bla  from bla, bla directory








