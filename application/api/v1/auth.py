from flask_httpauth import HTTPBasicAuth
from application.auth.models import User
from flask import g
from .error import unauthorized
auth=HTTPBasicAuth()

@auth.verify_password
def verify_password(email,password):
    if email=="":
        return False
    user=User.query.filter_by(email=email).first()
    if not user:
        return False
    g.current_user=user
    return user.verify_password(password)

@auth.error_handler
def auth_error():
    return unauthorized("Invalid Credentials")