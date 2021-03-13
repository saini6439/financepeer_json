# financepeer_json

## Local setup instructions
+ Clone the project from source
```shell
https://github.com/saini6439/financepeer_json.git && cd financepeer_json
```
+ Setup virtual environment
```shell
pip install virtualenv
virtualenv venv --python=python3.7
```
Now activate the environment shell with:
```shell
source venv/bin/activate  # On Linux
```
or
```bat
venv\Scripts\activate  & :: On Windows
```
+ Install all dependencies
```shell
pip install -r requirements.txt
```

+ Database migrations
```
cd financepeerasg
python manage.py makemigrations
python manage.py migrate
```


+ Finally! Run server
```
python manage.py runserver
```

Open [localhost:8000](http://localhost:8000)

+ To access Django Admin
```
python manage.py createsuperuser
```

When prompted, type your username (lowercase, no spaces), email address, and password.
For example, the output should look like this:

```
Username: nomadadmin
Email address: nomadadmin@nomad.com
Password:
Password (again):
Superuser created successfully.
```


Else you can use:
```
Username : jagdish
Password : admin@123
```
+ Re-run the server
```
python manage.py runserver
```

Open [localhost:8000/login](http://localhost:8000/login)
Create a account and login using that account after that upload your json file and then data is uploaded in visible to you.

