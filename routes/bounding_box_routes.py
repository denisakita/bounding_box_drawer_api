import json
import os

from flask import Blueprint, request, jsonify

from config import IMAGE_DIR

bounding_box_routes = Blueprint('bounding_box_routes', __name__)


@bounding_box_routes.route('/save', methods=['POST'])
def save_bounding_boxes():
    data = request.json
    image_name = data.get('imageName')
    bounding_boxes = data.get('boundingBoxes')

    if not image_name:
        return jsonify({"error": "Image name or bounding boxes missing"}), 400

    json_path = os.path.join(IMAGE_DIR, f'{os.path.splitext(image_name)[0]}.json')
    with open(json_path, 'w') as f:
        json.dump(bounding_boxes, f)

    return jsonify({"message": "Bounding boxes saved successfully"}), 200


@bounding_box_routes.route('/load', methods=['GET'])
def load():
    image_name = request.args.get('imageName')
    base_name = os.path.splitext(image_name)[0]
    json_path = os.path.join(IMAGE_DIR, f'{base_name}.json')
    image_url = f'http://localhost:5000/api/images/{image_name}'

    if not os.path.isfile(json_path):
        return jsonify({"boundingBoxes": []}), 200

    with open(json_path, 'r') as f:
        bounding_boxes = json.load(f)

    return jsonify({"boundingBoxes": bounding_boxes, "imageUrl": image_url}), 200
