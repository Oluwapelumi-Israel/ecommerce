
import jwt
from account.models import EcommerceUsers
from converter.dbdata_to_json import DataConverter
from exceptions.usererror import EcommerceUserError


class GetData(DataConverter):
    Model= EcommerceUsers
    keys = ["accesskey"]



    @classmethod
    def decode_access_token(cls):
        
        user = jwt.decode(jwt=cls.Model_key['accesskey'], key='access_token', algorithms='HS256')

        if user != None:
          return user
        else:
            raise EcommerceUserError("Invalid Credentials")
    


    def decode_refresh_token(cls):
        user = jwt.decode(jwt=cls.Model_key['refreshkey'], key='refresh_token', algorithms='HS256')

        return user['email']