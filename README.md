# Bounding Box Drawer Backend

## Overview

This project is the backend component of the Bounding Box Drawer application. It is built with Python and Flask to
support the frontend in drawing, saving, and managing bounding boxes on images. The backend handles image storage,
bounding box data management, and serves necessary API endpoints.

## Features

- RESTful API endpoints for saving, loading, and retrieving images and their bounding boxes.
- Supports basic image management operations.
- JSON-based responses.
- Easy integration with frontend.

## Table of Contents

1. [Installation](#installation)
2. [Configuration](#configuration)
3. [Running the Application](#running-the-application)
4. [Project Structure](#project-structure)
5. [API Endpoints](#api-endpoints)
6. [License](#license)

## Installation

### Prerequisites

- Python 3.12
- [pip](https://pip.pypa.io/en/stable/)
- [Flask](https://flask.palletsprojects.com/)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/bounding-box-drawer-backend.git
   cd bounding-box-drawer-backend
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Configuration settings for the application can be found in the `config.py` file. This includes settings for the storage
location and other environment variables.

## Running the Application

1. **Start the Flask development server:**

   ```bash
   flask run
   ```

2. **Access the application:**

   The backend does not have a user interface, but the API can be accessed
   at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Project Structure

Here's a brief overview of the project structure:

```
bounding-box-drawer-backend/
├── app.py
├── images/
├── routes/
│   ├── bounding_box_routes.py
│   ├── image_routes.py
├── config.py
├── venv/
├── .gitignore
├── README.md
└── requirements.txt
```

## API Endpoints

### Bounding Box Management

#### **POST `/save`**

- **Description**: Saves bounding box coordinates for a given image.
- **Request Body**:
  ```json
  {
      "imageName": "image_name.png",
      "boundingBoxes": [
          {"x": 30, "y": 40, "width": 100, "height": 120}
      ]
  }
  ```
- **Response**:
  ```json
  {
      "message": "Bounding boxes saved successfully"
  }
  ```

#### **GET `/load`**

- **Description**: Loads bounding boxes for a specified image.
- **Query Parameters**: `imageName`
- **Response**:
  ```json
  {
      "boundingBoxes": [
          {"x": 30, "y": 40, "width": 100, "height": 120}
      ],
      "imageUrl": "http://localhost:5000/api/images/image_name.png"
  }
  ```

### Image Management

#### **POST `/upload`**

- **Description**: Handles image upload.
- **Form Data**:
    - `image` (file)
- **Response**:
  ```json
  {
      "message": "Image uploaded successfully"
  }
  ```

#### **GET `/overview`**

- **Description**: Provides an overview of all uploaded images.
- **Response**:
  ```json
  {
      "images": ["image_name1.png", "image_name2.jpg"]
  }
  ```

#### **GET `/images/<filename>`**

- **Description**: Retrieves an uploaded image file by filename.
- **Path Parameter**: `filename` (string)
- **Response**: The requested image file or a 404 error if the file is not found.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.