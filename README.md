    ## Name: Courses
    ## Description:
    Web API para la gestión de cursos.
    ## Platform: Web API
    ## Technologies: Django - PostgreSQL
    ## Version: 1.0.0
    ## API URL
    [https://django-courses-migueldev81.herokuapp.com/api/v1](https://django-courses-migueldev81.herokuapp.com/api/v1)
    ## Swagger Documentation
    [https://django-courses-migueldev81.herokuapp.com/api/v1](https://django-courses-migueldev81.herokuapp.com/api/v1)
    ## Database | SQL
    ![database](./resources/database.png)
    ## Local Development
   ### Requerimients
```
Python
PostgreSQL
```
### Variables Enviroment (.env)
````
DB_DATABASE=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
SECRET_KEY = 
````
### SQL Console(No Remote)
````
CREATE DATABASE [DB_DATABASE];
````
### Virtual Enviroment
```
cd venv 
```
```
cd scripts>activate
```
```
pip install -r requirements.txt
```

### Start Project
```
python manage.py migrate
```
```
python manage.py runserver
```
