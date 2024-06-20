from flask import Flask
from flask_cors import CORS

from routes import image_routes, bounding_box_routes

app = Flask(__name__)
CORS(app)  # Enable CORS

app.register_blueprint(image_routes, url_prefix='/api')
app.register_blueprint(bounding_box_routes, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
