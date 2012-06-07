from flask import Flask, request, Response

import backmongo


app = Flask(__name__)
    
@app.route("/<collection>/", methods=['GET'])
@app.route("/<collection>/<id>", methods=['GET'])
def read(collection, id=None):
    result = backmongo.read(collection, id)
    return Response(result, mimetype='application/json')

@app.route("/<collection>/<id>", methods=['DELETE'])
def delete(collection, id):
    backmongo.delete(collection, id)
    return Response("{status: OK}", mimetype='application/json')

@app.route("/<collection>/", methods=['POST'])
@app.route("/<collection>/<id>", methods=['PUT'])
def save(collection, id=None):
    result = backmongo.save(collection, request.json, id)
    return Response(result, mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True)