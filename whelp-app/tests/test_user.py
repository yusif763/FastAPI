from urllib import response
from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# def test_create_user():
#     response = client.post(
#         "/api/v1/signup/",
#         json={"email": "test_user@gmail.com", 
#         "username": "test_user", 
#         "password": "test_user"}
#     )
#     assert response.status_code == 201

def test_login():
    response = client.post(
    "/api/v1/login/",
     json={"email": "dadddsjjj@gmail.com", 
        "password": "salaaaaaam"}
    )
    assert response.status_code == 200