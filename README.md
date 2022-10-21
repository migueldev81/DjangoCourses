    
   <table id="vertical-1">
        <caption></caption>
        <tr>
            <th>NAME</th>
            <td>Courses</td>
        </tr>
        <tr>
            <th>DESCRIPTION</th>
            <td>Desarrollo de API REST para la gestión de cursos de un centro educativo. Esta API tiene fines de fortalecer conceptos en Python / Django REST FRAMEWORK. </td>
        </tr>
        <tr>
            <th>PLATFORM</th>
            <td>Web API</td>
        </tr>
        <tr>
            <th>TECHNOLOGIES</th>
            <td>Python / Django REST FRAMEWORK</td>
        </tr>
        <tr>
            <th>ARCHITECTURE</th>
            <td>REST</td>
        </tr>
        <tr>
            <th>AUTH</th>
            <td>JSON Web Token</td>
        </tr>
        <tr>
            <th>URL</th>
            <td><a href="http://localhost:8000/api/v1" target="_blank">http://localhost:8000/api/v1</a>
            </td>
        </tr>
        <tr>
            <th>DOCS</th>
            <td><a
                    href="http://localhost:8000/api-docs">http://localhost:8000/api-docs</a>
            </td>
        </tr>
   </table>

## Database | SQL
 ![database](./resources/db-design.png)
## Local Development
### Requerimients

Python
[https://www.python.org/downloads/](https://www.python.org/downloads/)

MySQL
[https://www.mysql.com/downloads/](https://www.mysql.com/downloads/)

### Git Repository
```
git clone https://github.com/migueldev81/django-courses
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
### Create Database | SQL Console
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
