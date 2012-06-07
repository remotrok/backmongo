import pymongo
import json
from bson import json_util
from pymongo.objectid import ObjectId

from backmongo_conf import DATABASE, OID_PREFIX


CONNECTION = pymongo.Connection()
DB = CONNECTION[DATABASE]

def clean_id(id):
    if id.startswith(OID_PREFIX):
        return ObjectId(id[len(OID_PREFIX):])
    else:
        return id

def dict_to_json_converter(obj, **kwargs):
    if isinstance(obj, ObjectId):
        return OID_PREFIX + str(obj)
    else:
        return json_util.default(obj, **kwargs)

def read(collection_name, id=None):
    if id is not None:
        result = DB[collection_name].find_one(clean_id(id))
    else:
        result = list(DB[collection_name].find())
    
    return json.dumps(result, default=dict_to_json_converter)

def delete(collection_name, id):
    DB[collection_name].remove(clean_id(id))

def save(collection_name, model, id=None):
    if id is not None:
        model['_id'] = clean_id(model['_id'])
    return DB[collection_name].save(model, manipulate=False)
