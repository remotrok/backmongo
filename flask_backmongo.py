from flask import Blueprint, request, Response

import backmongo

bp = Blueprint('api', __name__)

@bp.route("/<collection>/", methods=['GET'])
@bp.route("/<collection>/<id>", methods=['GET'])
def read(collection, id=None):
    result = backmongo.read(collection, id)
    return Response(result, mimetype='application/json')

@bp.route("/<collection>/<id>", methods=['DELETE'])
def delete(collection, id):
    backmongo.delete(collection, id)
    return Response("{status: OK}", mimetype='application/json')

@bp.route("/<collection>/", methods=['POST'])
@bp.route("/<collection>/<id>", methods=['PUT'])
def save(collection, id=None):
    result = backmongo.save(collection, request.json, id)
    return Response(result, mimetype='application/json')

def init_app(app, url_prefix=''):
    app.register_blueprint(bp, url_prefix=url_prefix)