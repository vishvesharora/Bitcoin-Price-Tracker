
# Bitcoin Price Tracker

You can get the live price of the bitcoin.

Whenever you fetch the live price it gets stored in a db along with the timestamp.

You can get all the stored prices with its timestamp.

### File structure
#### bitcoin/urls.py
contains all the urls(endpoints) that are being used in the project
#### bitcoin/models.py
contains the models(tables) used in project
#### bitcoin/views.py
contains the code of all the apis
#### bitcoin/settings.py
contains all the setting of the app



 


## Running Locally


To run this project locally you will have to install django and django rest framework

```bash
  pip install django
  pip install djangorestframework
  pip install requests
  python manage.py runserver
```
    
## API Reference

### Local URL

```bash
http://localhost:8000
```

#### Register 
Registration is required to acess the apis.
Returns a token that is used to acess the live and list api.

```http
  POST /register
```

| Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` |**required** username of the user |
| `password`      | `string` |**required** password of the user |

#### Login 
Login using username and password.
Returns a token that is used to acess the live and list api.

```http
  POST /login
```

| Body | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` |**required** username of the user |
| `password`      | `string` |**required** password of the user |



#### Get live price of bitcoin
```http
  GET /live
```

#### Get stored price with their timestamp

```http
  GET /list
```
 Query Paramter
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `page`      | `integer` | page no |








## Tech Stack


**Backend:** Django, Django REST framework



