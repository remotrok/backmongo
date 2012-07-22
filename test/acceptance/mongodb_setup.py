#! /usr/bin/env python

import pymongo

CONNECTION = pymongo.Connection()
DATABASE = "backmongo"

CONNECTION[DATABASE].drop_collection("collection_tests")
collection_tests = CONNECTION[DATABASE]['collection_tests']

collection_tests.insert({'_id': '1', 'name': 'manolo', 'age': 36})
collection_tests.insert({'_id': '2', 'name': 'silvio', 'age': 31})
