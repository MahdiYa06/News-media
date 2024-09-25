from django.db import models
from utils.base import TimeStampModel



class User(TimeStampModel):
    username = models.CharField(max_length=100, verbose_name='User name', unique=True, null=False, blank=False)
    password = models.CharField(max_length=30, verbose_name='User password', null=False, blank=False)
    phone_number = models.CharField(unique=True, null=False, blank=False, max_length=11)
    
    
    def __str__(self) -> str:
        return self.username
    
    
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
    email = models.EmailField("Email", max_length=254)
    gender = models.CharField("User's gender", choices=genders, max_length=1)
    date_of_birth = models.DateField("Birth date")
    profile_picture = models.ImageField("Profile image", upload_to='profiles/')
    
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} ({self.user.id})'
    
    
    class Meta:
        db_table = 'Profiles'