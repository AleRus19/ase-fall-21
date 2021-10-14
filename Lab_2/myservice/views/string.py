from flakon import JsonBlueprint
from flask import Flask, request, jsonify

string = JsonBlueprint('string', __name__)


@string.route('/string/concat', methods=['GET'])
def concat():
    #http://127.0.0.1:5000/string/concat?p=&q=
    m = str(request.args.get('p'))
    n = str(request.args.get('q'))
    return jsonify({'result':m+n})

