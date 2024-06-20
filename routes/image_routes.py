import os

from flask import Blueprint, request, jsonify, send_from_directory, abort

from config import IMAGE_DIR

image_routes = Blueprint('image_routes', __name__)


@image_routes.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files['image']
    image.save(os.path.join(IMAGE_DIR, image.filename))
    return jsonify({"message": "Image uploaded successfully"}), 200


@image_routes.route('/overview', methods=['GET'])
def image_overview():
    images = [f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    return jsonify({"images": images}), 200


@image_routes.route('/images/<filename>', methods=['GET'])
def get_image(filename):
    try:
        return send_from_directory(IMAGE_DIR, filename)
    except FileNotFoundError:
        abort(404, description="Image not found")
