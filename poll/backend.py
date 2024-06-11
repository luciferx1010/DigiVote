from poll.models import CustomUser
import logging
from django.conf import settings
from django.contrib.auth.hashers import check_password


'''
class MyAuthBackend:
    def authenticate(self,request,username, password):    
        try:
            user = CustomUser.objects.get(username=username)
            if user.check_password(password):
                return user
            else:
                return None
        except CustomUser.DoesNotExist:
            logging.getLogger("error_logger").error("user with login does not exists")
            return None
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            return None

    def get_user(self, user_id):
        try:
            user = CustomUser.objects.get(sys_id=user_id)
            if user.is_active:
                return user
            return None
        except CustomUser.DoesNotExist:
            logging.getLogger("error_logger").error("user with %(user_id)d not found")
            return None
'''

'''
class CustomUserBackend:
    
    def authenticate(self,request,username=None,password=None):
        if username and password:
            try:
                user = CustomUser.objects.get(username=username)
                if check_password(password,user.password):
                    if user.is_active:
                        return user
			except CustomUser.DoesNotExist:
				logging.getLogger("error_logger").error("User with login does not exists.")
                return None
        return None
    
    def get_user(self,user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
'''

class CustomUserBackend:

    def authenticate(self,request,username=None,password=None):
        if username and password:
            try:
                user = CustomUser.objects.get(username=username)
                if check_password(password,user.password):
                    if user.is_active:
                        return user
            except CustomUser.DoesNotExist:
                logging.getLogger("error_logger").error("User with login does not exists.")
                return None
        return None
    
    def get_user(self,user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None