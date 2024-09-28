Social Media API
A simple social media API built with Django and Django REST Framework. This project provides user authentication (registration, login, token generation) and a customizable user profile model.

Features
User registration
User login
Token-based authentication
Custom user model with bio, profile picture, and followers
Prerequisites
Before you begin, ensure you have the following installed:

Python 3.x
Django 3.x or later
Django REST Framework
Setup Instructions
Clone the Repository

Clone the repository from GitHub:

bash
Copy code
git clone https://github.com/your-username/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/social_media_api
Set Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies. Run the following commands:

bash
Copy code
python -m venv venv
source venv/bin/activate  # For Linux/Mac
# On Windows, use `venv\Scripts\activate`
Install Dependencies

Install Django, Django REST Framework, and other required dependencies:

bash
Copy code
pip install -r requirements.txt
Apply Migrations

Apply database migrations to set up the models and tables:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Run the Server

Start the Django development server:

bash
Copy code
python manage.py runserver
Access the API

Open your browser or use Postman to access the following endpoints:

http://localhost:8000/api/accounts/register/ (User Registration)
http://localhost:8000/api/accounts/login/ (User Login)
User Model
The project uses a custom user model that extends Django's AbstractUser. It includes the following additional fields:

bio: A text field where users can add a short biography.
profile_picture: An optional image field to upload a profile picture.
followers: A Many-to-Many relationship where users can follow other users (symmetrical=False, allowing one-sided follows).
The model is defined as follows:

python
Copy code
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.username
How to Register and Authenticate Users
1. User Registration
To register a new user, send a POST request to the registration endpoint:

Endpoint:
POST /api/accounts/register/

Sample Request Body:

json
Copy code
{
    "username": "john_doe",
    "password": "securepassword",
    "bio": "I love coding!",
    "profile_picture": null
}
If the registration is successful, a user token will be generated.

2. User Login
To log in a user and obtain an authentication token, send a POST request to the login endpoint:

Endpoint:
POST /api/accounts/login/

Sample Request Body:

json
Copy code
{
    "username": "john_doe",
    "password": "securepassword"
}
Response:

json
Copy code
{
    "token": "your-authentication-token"
}
Use this token for all authenticated API requests by including it in the Authorization header as a Bearer Token:

makefile
Copy code
Authorization: Token your-authentication-token
Testing
To test the API, you can use tools like Postman or curl.

Example curl request for login:

bash
Copy code
curl -X POST http://localhost:8000/api/accounts/login/ \
  -d "username=john_doe&password=securepassword"
Project Structure
bash
Copy code
social_media_api/
├── accounts/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py          # Custom User Model
│   ├── serializers.py     # User Serializer
│   ├── views.py           # Registration and Login Views
│   ├── urls.py            # API Endpoints for Accounts
├── social_media_api/
│   ├── __init__.py
│   ├── settings.py        # Project Settings
│   ├── urls.py            # Main URL Configuration
│   ├── wsgi.py
└── manage.py
License
This project is licensed under the MIT License. See the LICENSE file for details.








