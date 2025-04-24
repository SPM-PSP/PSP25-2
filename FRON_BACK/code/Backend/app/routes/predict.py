from flask import Blueprint, jsonify, abort
import os
import json
predict_bp = Blueprint('predict', __name__)

PREDICT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'data', 'result', 'result.json')
PREDICT_PATH = os.path.abspath(PREDICT_PATH)
print("PREDICT_PATH:", PREDICT_PATH)
@predict_bp.route('/predict/result', methods=['GET'])
def get_predict_result():
    if not os.path.exists(PREDICT_PATH):
        return abort(404, description="Result file not found")
    with open(PREDICT_PATH, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except Exception:
            return abort(500, description="Result file format error")
    return jsonify(data)


