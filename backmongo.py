import pymongo
import json
from bson import json_util
from pymongo.objectid import ObjectId

CONNECTION = pymongo.Connection()
DATABASE = "backmongo"
DB = CONNECTION[DATABASE]

def dict_to_json_converter(obj, **kwargs):
    if isinstance(obj, ObjectId):
        return str(obj)
    else:
        return json_util.default(obj, **kwargs)

def read(collection_name, id=None):
    if id is not None:
        result = DB[collection_name].find_one(ObjectId(id))
    else:
        result = list(DB[collection_name].find())
    
    return json.dumps(result, default=dict_to_json_converter)

def delete(collection_name, id):
    DB[collection_name].remove(ObjectId(id))

def save(collection_name, model, id=None):
    if id is not None:
        model['_id'] = ObjectId(model['_id'])
    return DB[collection_name].save(model, manipulate=False)
