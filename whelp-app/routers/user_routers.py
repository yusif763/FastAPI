import json
from main import app
from models.user_model import User
import schemas.user_shemas as user_schema
from fastapi import APIRouter
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi import FastAPI, HTTPException, Depends, Request
from passlib.context import CryptContext


router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post('/signup/',response_model=user_schema.User,status_code=201)
def create_user(user:user_schema.UserCreate):
    password = pwd_context.hash(user.password)
    print(password)
    new_user = User(email=user.email,username=user.username,password=password)
    new_user.save()
    return new_user



@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


@router.post('/login/',response_model=user_schema.UserLoginResponseSchema,status_code=200)
def login(user: user_schema.UserLogin, Authorize: AuthJWT = Depends()):
    old_user = User.filter(User.email == user.email).first()
    pass_bool=pwd_context.verify(user.password, old_user.password)
    if user.email != old_user.email or not pass_bool:
        raise HTTPException(status_code=401,detail="Bad username or password")

    access_token = Authorize.create_access_token(subject=old_user.username)
    refresh_token = Authorize.create_refresh_token(subject=old_user.username)
    return {"user":old_user.email,"access_token": access_token,'refresh_token':refresh_token}


@router.post('/refresh')
def refresh(Authorize: AuthJWT = Depends()):

    Authorize.jwt_refresh_token_required()

    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token}


@router.get('/user')
def protected(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    current_user = Authorize.get_jwt_subject()
    current_user = User.filter(username=current_user).first()
    current_user.__data__.pop("password")
    return {"user": current_user.__data__}