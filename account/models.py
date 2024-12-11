from django.db import models
from exceptions.usererror import EcommerceUserError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import jwt, datetime
from datetime import timezone
# Create your models here.


class EcommerceUsersManager(BaseUserManager):
    def create_users(self, email, first_name, last_name, password, user_role):
        if email == None or email == '':
            raise EcommerceUserError(message='email field cannot be empty')
        if first_name == None or first_name == '':
            raise EcommerceUserError(message='first name field cannot be empty')
        if last_name == None or last_name == '':
            raise EcommerceUserError(message='last name field cannot be empty')
        if password == None or password == '':
            raise EcommerceUserError(message='password field cannot be empty')
        if user_role == None or user_role == '':
            raise EcommerceUserError(message='User role field cannot be empty')

        email = self.normalize_email(email=email)


        user = self.model(email=email, first_name=first_name, last_name=last_name, user_role=user_role)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    

    def create_superuser(self, email, first_name, last_name, password, user_role):
        user = self.create_users(
                        email=email, 
                        first_name=first_name, 
                        last_name=last_name, 
                        password=password, 
                        user_role=user_role
                          )
        user.is_superuser = True
        user.is_staff = True
        user.is_verified = True
        user.save(using=self._db)
        return user
    


class EcommerceUsers(AbstractBaseUser, PermissionsMixin):

    ECOMMERCE_USER_CATEGORY = {
        1: 'BUYER',
        2: 'SELLER'
    }

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    user_role = models.IntegerField(choices=ECOMMERCE_USER_CATEGORY)
    user_image = models.FileField(upload_to="documents", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    

    objects = EcommerceUsersManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["first_name", "last_name", "user_role"]

    def generate_access_token(self):
        payload = {
            'email': self.email,
            'exp': datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(minutes=10),
            'iat': datetime.datetime.now(tz=timezone.utc)
        }

        access_token = jwt.encode(payload=payload, key='access_token', algorithm='HS256').encode('utf-8')
        return access_token



    def generate_refresh_token(self):
        payload = {
            'email': self.email,
            'exp': datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(days=3),
            'iat': datetime.datetime.now(tz=timezone.utc)
        }

        refresh_token = jwt.encode(payload=payload, key='refresh_token', algorithm='HS256').encode('utf-8')
        return refresh_token
    

   