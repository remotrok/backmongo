#! /usr/bin/env python

import pymongo
from pymongo.objectid import ObjectId

CONNECTION = pymongo.Connection()
DATABASE = "backmongo"

CONNECTION[DATABASE].drop_collection("collection_tests")
collection_tests = CONNECTION[DATABASE]['collection_tests']

collection_tests.insert({'_id': ObjectId('4f6b75e052ad624ff62cfc8b'), 'name':'manolo', 'age':36})
collection_tests.insert({'_id': ObjectId('4f6b75e952ad624ff62cfc8c'), 'name':'silvio', 'age':31})
