## Summary:
Python JWT authentication in Django Rest Framework with Postgres database.

It contains the following apps:
- authentication (implements authentication)
- example (uses authentication)

## Requirements:
```
Python==3.5.1
Django==2.0.10
djangorestframework==3.7.7
psycopg2==2.7.3
PyJWT==1.7.1
```

## Project Structure (App Based):
```bash
DjangoRestJWTAuthentication/
├── apps
│   ├── authentication
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── authentication.py
│   │   ├── permission.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── example
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── urls.py
│   │   └── views.py
│   └── jwt_utility.py
├── django_rest_jwt
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── README.md
├── manage.py
└── requirements.txt
```
### How to start application (using Virtual Environment)
- Clone the project using command:
    ```
    git clone https://github.com/Rabia23/DjangoRestJWTAuthentication.git
    ```
- Go into the project directory:
    ```
    cd DjangoRestJWTAuthentication
    ```
- Create and Activate the Virtual Environment:
  ```
  virtualenv <name of the environment> e.g virtualenv venv_jwt
  source venv_jwt/bin/activate
  ```
- Install requirements:
  ```
  pip install -r requirements.txt
  ```
Note: You can see your installed dependencies by running command: ```pip freeze```
- Run the Application:
  ```
  ./manage.py runserver
  ```
  
### Test using POSTMAN
- http://127.0.0.1:8000/api/auth/login/
```
{"id": 2, "username": "rabia", "email": "", "first_name": "", "last_name": "", "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InJhYmlhIiwiZXhwIjoxNTUxMjA4Mjc5fQ.I89J-LRu70IkgxzPcEzRAw8uGN1lK2h_txpsgzJ2B8E"}
```
- http://127.0.0.1:8000/api/auth/register/
```
{"id": 2, "username": "rabia", "email": "", "first_name": "", "last_name": ""}
```
- http://127.0.0.1:8000/api/ (using Bearer Token as Authorization Type)
```
{"message": "Welcome rabia iftikhar"}
```

### Userful Links
- https://pypi.org/project/jwt/
- https://pyjwt.readthedocs.io/en/latest/


