import json
import os

from flask import Blueprint, request, jsonify

from config import IMAGE_DIR

bounding_box_routes = Blueprint('bounding_box_routes', __name__)


def validate_bounding_boxes(bounding_boxes):
    """Validate the structure of bounding boxes data."""
    if not isinstance(bounding_boxes, list):
        return False
    for box in bounding_boxes:
        if not all(key in box for key in ['x', 'y', 'width', 'height']):
            return False
        if not all(isinstance(box[key], (int, float)) for key in ['x', 'y', 'width', 'height']):
            return False
    return True


@bounding_box_routes.route('/save', methods=['POST'])
def save_bounding_boxes():
    """Save bounding boxes to a JSON file associated with an image."""
    data = request.json
    image_name = data.get('imageName')
    bounding_boxes = data.get('boundingBoxes')

    if not image_name or not validate_bounding_boxes(bounding_boxes):
        return jsonify({"error": "Image name or bounding boxes missing or invalid"}), 400

    json_path = os.path.join(IMAGE_DIR, f'{os.path.splitext(image_name)[0]}.json')
    try:
        with open(json_path, 'w') as f:
            json.dump(bounding_boxes, f)
        return jsonify({"message": "Bounding boxes saved successfully"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to save bounding boxes: {str(e)}"}), 500


@bounding_box_routes.route('/load', methods=['GET'])
def load_bounding_boxes():
    """Load bounding boxes from a JSON file associated with an image."""
    image_name = request.args.get('imageName')
    if not image_name:
        return jsonify({"error": "Image name missing"}), 400

    base_name = os.path.splitext(image_name)[0]
    json_path = os.path.join(IMAGE_DIR, f'{base_name}.json')
    image_url = f'http://localhost:5000/api/images/{image_name}'

    if not os.path.isfile(json_path):
        return jsonify({"boundingBoxes": [], "imageUrl": image_url}), 200

    try:
        with open(json_path, 'r') as f:
            bounding_boxes = json.load(f)
        return jsonify({"boundingBoxes": bounding_boxes, "imageUrl": image_url}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to load bounding boxes: {str(e)}"}), 500
