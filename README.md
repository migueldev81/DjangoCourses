    
   <table id="vertical-1">
        <caption></caption>
        <tr>
            <th>NAME</th>
            <td>Courses</td>
        </tr>
        <tr>
            <th>DESCRIPTION</th>
            <td>Web API for courses </td>
        </tr>
        <tr>
            <th>PLATFORM</th>
            <td>Web API</td>
        </tr>
        <tr>
            <th>ARCHITECTURE</th>
            <td>REST</td>
        </tr>
        <tr>
            <th>AUTH</th>
            <td>Yes</td>
        </tr>
        <tr>
            <th>TECHNOLOGIES</th>
            <td><img src="https://img.icons8.com/color/48/000000/python--v1.png"/> <img src="https://img.icons8.com/color/48/000000/django.png"/> <img src="https://img.icons8.com/color/48/000000/mysql-logo.png"/></td>
        </tr>
        <tr>
            <th>API URL</th>
            <td><a href="https://node-alkemy-challenge.onrender.com/api/v1" target="_blank">https://node-alkemy-challenge.onrender.com/api/v1</a>
            </td>
        </tr>
        <tr>
            <th>DOCS</th>
            <td><a
                    href="https://node-alkemy-challenge.onrender.com/api-docs">https://node-alkemy-challenge.onrender.com/api-docs</a>
            </td>
        </tr>
        <tr>
            <th>MOBILE</th>
            <td><a href="https://www.w3schools.com" target="_blank">Visit W3Schools</a></td>
        </tr>
   </table>

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
