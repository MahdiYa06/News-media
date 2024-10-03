from django.db import models
from utils.base import TimeStampModel
from django.contrib.auth.models import AbstractUser, BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError("Users must have a Phone number")
        
        user = self.model(
            phone_number = phone_number,
            
        )
        
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password=None):
        if not phone_number:
            raise ValueError("Users must have a Phone number")
        
        user = self.model(
            phone_number = phone_number,
            
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        return user



class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = None
    
    phone_number = models.CharField("Phone number", max_length=20, unique=True)
    
    USERNAME_FIELD = 'phone_number'
    
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def __str__(self) -> str:
        return self.phone_number
    
    
    class Meta:
        db_table = 'Users'


class Profile(TimeStampModel):
    
    genders = {
        'M':'male',
        'F':'female'
    }
    
    user = models.OneToOneField('user.User', on_delete=models.CASCADE, related_name='profile')   
    first_name = models.CharField('First name', max_length=100)
    last_name = models.CharField('Last name', max_length=100)
    email = models.EmailField("Email", max_length=254, unique=True)
    gender = models.CharField("User's gender", choices=genders, max_length=1)
    date_of_birth = models.DateField("Birth date")
    profile_picture = models.ImageField("Profile image", upload_to='profiles/')
    
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} ({self.user.id})'
    
    
    class Meta:
        db_table = 'Profiles'
        
    