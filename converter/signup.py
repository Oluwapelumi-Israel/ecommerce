from converter.dbdata_to_json import DataConverter
from account.models import EcommerceUsers
from exceptions.usererror import EcommerceUserError


class UserSerialiser(DataConverter):
    Model = EcommerceUsers
    keys = ["first_name", "last_name", "user_image", "user_role", "email", "password", "confirm_password"]

    @classmethod
    def validate(cls):
        if cls.Model_key['password'] == cls.Model_key['confirm_password']:
            return True
        else:
            return False

    #email, first_name, last_name, password, user_role, image=None
    @classmethod
    def save(cls):
        user = cls.Model_key
        if cls.validate():
            try:
                details = cls.Model.objects.create_users(email=user['email'],
                                                      first_name=user['first_name'],
                                                      last_name=user['last_name'],
                                                      password=user['password'],
                                                      user_role=user['user_role'],
                                                      )
                
            except EcommerceUserError as e:
                raise EcommerceUserError(message=repr(e))
            else:
                details.user_image = user['user_image']
                details.save()
                return details
        else:
            raise EcommerceUserError(message="the password entered are not the same")




    