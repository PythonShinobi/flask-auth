# Flask-Auth

Flask-Auth is a secure authentication system built with Flask. It provides robust user authentication functionalities, including password recovery via email, access control to routes only for logged-in users, and secure password hashing in the database. Additionally, it implements a feature where users are redirected to the originally requested page after successful login.

## Features

* User registration with email verification.
* Secure password hashing using industry-standard algorithms.
* Password recovery mechanism with email notification.
* Access control: Users can only access certain routes when logged in.
* Redirection to the originally requested page after successful login.


## Installation

1. Clone the repository:
   git clone `<https://github.com/PythonShinobi/flask-auth.git>`
2. Install dependencies:

   pip install -r requirements.txt


## Usage

1. Configure your Flask application and set up the necessary environment variables (e.g., database settings, email configuration) in `config.py`.
2. Initialize and migrate the database:

   flask db init
   flask db migrate
   flask db upgrade
3. Start the Flask application:

   flask run


## Configuration

* `config.py`: Configure database settings, email settings, secret key, etc.


## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Flask
* Flask-Login
* Flask-WTF
* Flask-Mail
* Flask-SQLAlchemy

## Contact

For questions or support, please contact **pythonshinobi@gmail.com**
