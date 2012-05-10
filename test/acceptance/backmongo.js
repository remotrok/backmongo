var assert = require('assert');
var should = require('should');
var jQuery = require("jquery");
var Backbone = require('backbone');

Backbone.setDomLibrary(jQuery);

var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

jQuery.support.cors = true;
jQuery.ajaxSettings.xhr = function () {
    return new XMLHttpRequest;
}

var BMModel = Backbone.Model.extend({
    idAttribute: "_id",
    urlRoot: 'http://localhost:5000/collection_tests/'
});

var BMCollection = Backbone.Collection.extend({
    model: BMModel,
    url: 'http://localhost:5000/collection_tests/'         
});


describe("BMCollection", function(){
    var bmcollection;

    beforeEach(function(){
         bmcollection = new BMCollection();
    });  
        
    it("is defined", function(){
        bmcollection.should.not.equal(undefined);
    });
});

describe("BackMongo", function(){
    var bmcollection = new BMCollection();

    describe("read all", function(){
        var expected;
   
        beforeEach(function(done){
            bmcollection.fetch({success: function(){
                done();
            }});
        });

        it("gets contents from mongo", function(){
            bmcollection.models.should.have.lengthOf(2);
        });

        it("has this models", function(){
            expected = [
                {
                    "_id": "4f6b75e052ad624ff62cfc8b",
                    "name": "manolo",
                    "age": 36
                },
                {
                    "_id": "4f6b75e952ad624ff62cfc8c",
                    "name": "silvio",
                    "age": 31
                }
            ];
            for(var i=0; i<2; i++){
                expected[i].name.should.equal(bmcollection.models[i].get('name'));
                expected[i].age.should.equal(bmcollection.models[i].get('age'));
                expected[i]._id.should.equal(bmcollection.models[i].get('_id'));
                expected[i]._id.should.equal(bmcollection.models[i].id);
            }
        });
    });

    describe("read one", function(){
        var model;

        before(function(done){
            model = new BMModel({_id: '4f6b75e952ad624ff62cfc8c'});
            model.fetch({success: function(){done();}});
        });

        it("fetchs a given model", function(){
            model.get('name').should.equal("silvio");
            model.get('age').should.equal(31);
        });
    });

    describe("create", function(){
        before(function(){
            bmcollection.create({
                "name": "paco",
                "age": 32
            }, {success: function(){done();}});
        });

        before(function(done){
            bmcollection.fetch({success: function(){done();}});
        });

        it("adds a new model to collection", function(){
            bmcollection.models.should.have.lengthOf(3);
        });

        it("adds the correct model", function(){
            var model = bmcollection.find(function(model){
                return model.get('name') == 'paco';
            });
            should.exist(model);     
        });
    });

    describe("delete", function(){
        before(function(done){
            bmcollection.fetch({success: function(){done();}});
        });

        before(function(){
            var model = bmcollection.get('4f6b75e952ad624ff62cfc8c');
            model.destroy({success: function(){done();}});
        });

        before(function(done){
            bmcollection.fetch({success: function(){done();}});
        });

        it("there is one model less in collection", function(){
            bmcollection.models.should.have.lengthOf(2);
        });

        it("deletes the right one", function(){
            var model = bmcollection.find(function(model){
                return model.get('_id') == '4f6b75e952ad624ff62cfc8c';
            });
            should.not.exist(model);     
        });
    });

    describe("update", function(){
        before(function(done){
            bmcollection.fetch({success: function(){done();}});
        });

        before(function(){
            var model = bmcollection.get('4f6b75e052ad624ff62cfc8b');
            model.set('name', 'pepito');
            model.save({success: function(){done();}});
        });

        before(function(done){
            bmcollection.fetch({success: function(){done();}});
        });

        it("update the right one", function(){
            var model = bmcollection.find(function(model){
                return model.id == '4f6b75e052ad624ff62cfc8b' && 
                    model.get('name') == 'pepito' && model.get('age') == 36;
            });
            should.exist(model);     
        });
    });
});
