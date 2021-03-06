from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import MaxValueValidator
from django.utils.timezone import now
from datetime import datetime

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        
        if not email:
            raise ValueError('Users must have an email address')

        account = self.model(
            email=self.normalize_email(email),

        )
        account.account_type = extra_fields.get('account_type')
        account.set_password(password)
        account.save(using=self._db)
        return account

    def create_superuser(self, email, password, **extra_fields):
        
        account = self.create_user(
            email,
            password=password,
        )
        account.account_type = 'A'
        account.is_admin = True
        account.save(using=self._db)
        return account


class Account(AbstractBaseUser):
    name=models.CharField(blank=True,null=True,max_length=255)
    
    type_choice = (
                   ('A', 'Admin'),
                   ('S','Student'),
                   ('T','Teacher'),
                   )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    account_type = models.CharField(choices=type_choice, max_length=1, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
         return True

    @property
    def is_staff(self):
        return self.is_admin

# class Student(models.Model):
#     name=models.CharField(blank=True,null=True,max_length=255)
#     Address=models.CharField(blank=True,null=True,max_length=255)
#     mobile=models.CharField(blank=True,null=True,max_length=255)

#     def __str__(self):
#         return self.name


# class Teacher(models.Model):
#     name=models.CharField(blank=True,null=True,max_length=255)
#     Address=models.CharField(blank=True,null=True,max_length=255)
#     Suject=models.CharField(blank=True,null=True,max_length=255)
#     mobile=models.CharField(blank=True,null=True,max_length=255)


#     def __str__(self):
#         return self.name