# MODU FORUM API

## 📌 How to Install the "Modu Forum API" Project
```
# Create a New Folder for Project
mkdir project_folder

# Create a Virtual Environment 
cd project_folder 
python -m venv venv

# Activate the Virtual Enviroment
source project_folder\venv\Scripts\activate
if below line shows up, virtual environment has been successfully created
(venv) C:\> 

# Install Required Packages
pip install -r requirements.txt

# Migrate Tables
python manage.py makemigrations 
python manage.py migrate

# Create Admin Account
python manage.py createsuperuser

# Run Server
python manage.py runserver


```
## 📌 Features

## Show Question Post

- **URL**

    /api

- **Method:**

    `GET`

- **URL Params**
    - **Required:** None

- **Request Header:**
    - Allow: GET 
    - Content-Type: application/json


- **Success Response:**
    - **Code:** 200 OK
    - **Content:** `[{"id":1,"title":"hello","author":1,"excerpt":"hi","content":"...","published":"2021-07-23T18:48:00Z","likes":[1]}]`
    
  
- **Error Response:**
    - **Code:** 404
    - **Content:** `{ error : "POST DOES NOT EXIST" }`

    -------------------------------------------------------------------------

## Save New Question Post

- **URL**

    /api/create-post

- **Method:**

    `POST`

- **URL Params**
    - **Required:** None
    

- **Request Header:**
    - Allow: POST 
    - Content-Type: application/json


- **Success Response:**
    - **Code:** 200 OK
    - **Content:** `[{"id":2,"title":"new post","author":1,"excerpt":"test","content":"...","published":"2021-07-23T18:48:00Z","likes":[1]}]`
    
  
- **Error Response:**
    - **Code:** 400

    -------------------------------------------------------------------------

## Edit Question Post

- **URL**

    /api/edit/pk/

- **Method:**

    `PUT`


- **URL Params**
    - **Required:** None

- **Request Header:**
    - Allow: PUT
    - Content-Type: application/json


- **Success Response:**
    - **Code:** 200 OK
    - **Content:** `[{"id":2,"title":"update post","author":1,"excerpt":"test","content":"...","published":"2021-07-23T18:48:00Z","likes":[1]}]`
    
  
- **Error Response:**
    - **Code:** 400

    -------------------------------------------------------------------------

## Delete Question Post

- **URL**

    /api/delete/pk/

- **Method:**

    `DELETE`


- **URL Params**
    - **Required:** None

- **Request Header:**
    - Allow: DELETE 
    - Content-Type: application/json


- **Success Response:**
    - **Code:** 200 OK
    
  
- **Error Response:**
    - **Code:** 400

    -------------------------------------------------------------------------


## Show Comment of a Post

- **URL**

    /api/comment/pk/

- **Method:**

    `GET`

- **URL Params**
    - **Required:** None

- **Request Header:**
    - Allow: GET 
    - Content-Type: application/json


- **Success Response:**
    - **Code:** 200 OK
    - **Content:** `[{"id": 1, "post": 10, "name": "testuser", "content": "...", "published": "2021-07-23T11:47:07Z"}]`
    
  
- **Error Response:**
    - **Code:** 404
    - **Content:** `{ error : "POST DOES NOT EXIST" }`

    -------------------------------------------------------------------------

## Save Comment of a Post

- **URL**

    /api/create-comment/pk

- **Method:**

    `GET`


- **URL Params**
    - **Required:** None

- **Request Header:**
    - Allow: GET 
    - Content-Type: application/json


- **Success Response:**
    - **Code:** 200 OK
    - **Content:** `{"id":1,"title":"hello","author":1,"excerpt":"hi","content":"...","published":"2021-07-23T18:48:00Z","likes":[1]}]`
    
  
- **Error Response:**
    - **Code:** 400

    -------------------------------------------------------------------------

## Search by Title or Content Keyword of a Post

- **URL**

    /api/search/?search=test

- **Method:**

    `GET`

- **URL Params**

    **Required:**
    - `search=[string]`


- **Request Header:**
    - Allow: GET 
    - Content-Type: application/json


- **Success Response:**
    - **Code:** 200 OK
    - **Content:** `{"id":1,"title":"hello","author":1,"excerpt":"hi","content":"...","published":"2021-07-23T18:48:00Z","likes":[1]}]
    or [ ]`
  
