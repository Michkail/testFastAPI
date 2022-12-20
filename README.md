# RESTful test using FastAPI

## Requirement:
### u can use pip or pipenv for install the library
```
- python-jose
- passlib
- python-multipart
- fastapi
- uvicorn
- schemas
- pydantic
- beanie
- email-validator
- python-decouple
- pymongo==3.12.1
```

## Generate token using JSON Web Token
### Step 1, create user:
![This is an image](/assets/create-user-before.png)

###### After exec
![This is an image](/assets/create-user-after.png)


### Step 2, generate token:
![This is an image](/assets/generate-token-before.png)

###### After exec
![This is an image](/assets/generate-token-after.png)


### Step 3, auth for verify token
![This is an image](/assets/auth.png)

###### Pop-up form
![This is an image](/assets/auth-form.png)

###### Fill form
![This is an image](/assets/auth-form-filled.png)

###### After exec auth
![This is an image](/assets/auth-success.png)


### Step 4, verifying token test
![This is an image](/assets/test-token-before.png)
