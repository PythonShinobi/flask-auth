
from app import create_app

# Create the Flask application using the create_app function
flask_app = create_app()

if __name__ == '__main__':
    flask_app.run(port=5001)