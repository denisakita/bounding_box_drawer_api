import os

from flask import Blueprint, request, jsonify, send_from_directory, abort
from werkzeug.utils import secure_filename

from config import IMAGE_DIR

image_routes = Blueprint('image_routes', __name__)

# Allowed extensions for uploaded images
ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png'}


def allowed_file(filename):
    """Check if a file is allowed based on its extension."""
    return '.' in filename and os.path.splitext(filename)[1].lower() in ALLOWED_EXTENSIONS


@image_routes.route('/upload', methods=['POST'])
def upload_image():
    """Handle image upload and save it to the IMAGE_DIR."""
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files['image']

    if image.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if allowed_file(image.filename):
        filename = secure_filename(image.filename)
        try:
            image.save(os.path.join(IMAGE_DIR, filename))
            return jsonify({"message": "Image uploaded successfully"}), 200
        except Exception as e:
            return jsonify({"error": f"Failed to save image: {str(e)}"}), 500
    else:
        return jsonify({"error": "Unsupported file type"}), 400


@image_routes.route('/overview', methods=['GET'])
def image_overview():
    """Return a list of image filenames available in IMAGE_DIR."""
    try:
        images = [f for f in os.listdir(IMAGE_DIR) if allowed_file(f)]
        return jsonify({"images": images}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to list images: {str(e)}"}), 500


@image_routes.route('/images/<filename>', methods=['GET'])
def get_image(filename):
    """Serve an image file from the IMAGE_DIR."""
    try:
        return send_from_directory(IMAGE_DIR, filename)
    except FileNotFoundError:
        abort(404, description="Image not found")
    except Exception as e:
        abort(500, description=f"Error retrieving image: {str(e)}")
