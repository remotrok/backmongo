from flask import Blueprint, request, Response, Flask

import backmongo

bp = Blueprint('api', __name__)


@bp.route("/<collection>/", methods=['GET'])
@bp.route("/<collection>/<_id>", methods=['GET'])
def read(collection, _id=None):
    result = backmongo.read(collection, _id)
    return Response(result, mimetype='application/json')


@bp.route("/<collection>/<_id>", methods=['DELETE'])
def delete(collection, _id):
    backmongo.delete(collection, _id)
    return Response("{status: OK}", mimetype='application/json')


@bp.route("/<collection>/", methods=['POST'])
@bp.route("/<collection>/<_id>", methods=['PUT'])
def save(collection, _id=None):
    result = backmongo.save(collection, request.json, _id)
    return Response(result, mimetype='application/json')


def init_app(app, url_prefix=''):
    app.register_blueprint(bp, url_prefix=url_prefix)


def main():
    import sys
    import os
    static_folder = os.path.join(os.getcwd(), 'static')
    if len(sys.argv) > 1:
        static_folder = os.path.abspath(sys.argv[1])
    app = Flask('__main__',
            static_url_path='/static',
            static_folder=static_folder)
    init_app(app)
    app.run(debug=False)

if __name__ == '__main__':
    main()
