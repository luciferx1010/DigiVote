from django.db import models
#from django.contrib.auth.models import User
from datetime import date
#from django.contrib.auth.models import (AbstractUser,PermissionsMixin)
from ovs.settings import AUTH_USER_MODEL
#from django.utils import timezone

from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser, AbstractUser
)
from django.contrib.auth.models import PermissionsMixin

class CustomUserManager(BaseUserManager):
    #use_in_migrations= True

    def create_user(self, username, password,**extra_fields):
        if not username:
            raise ValueError("User must have User Name") 
        user = self.model(
			username = username,
            **extra_fields
		)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, username, password,**extra_fields):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username = username,
			password = password,
            **extra_fields
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password,**extra_fields):
        #extra_fields.setdefault('is_staff',True)
        #extra_fields.setdefault('is_superuser',True)
        #extra_fields.setdefault('is_active',True)
        user = self.create_user(
            username = username,
			password = password,
            **extra_fields
		)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user
		
class CustomUser(AbstractBaseUser):

    aadharnumber=models.CharField(max_length=12,null=False,unique=True)
    Mobilenumber=models.CharField(max_length=10,unique=True,null=False)
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25,unique=True,null=False)
    first_name = models.CharField(max_length=150,null=False)
    last_name = models.CharField(max_length=150,null=False)
    email = models.EmailField(unique=True,null=False)
    password = models.CharField(max_length=150,null=False)
    dob = models.DateField(null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False) # a superuser
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name','aadharnumber','Mobilenumber','email','password']
    
    objects = CustomUserManager()


    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    def __str__(self):
        return "{} {}".format(self.username, self.email)
        
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin
    
    @property
    def is_anonymous(self):
        return False
        
    @property
    def is_authenticated(self):
        return True
    
    class Meta():
        db_table = 'auth_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Position(models.Model):
    title = models.CharField(max_length=50, unique=True)
    show_result = models.BooleanField(default=False)
    Election_on = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Candidate(models.Model):
    name = models.CharField(max_length=50)
    total_vote = models.IntegerField(default=0, editable=False)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Candidate Pic", upload_to='images/')

    def __str__(self):
        return "{} - {}".format(self.name, self.position.title)


class ControlVote(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {} - {}".format(self.user, self.position, self.status)
