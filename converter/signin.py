from account.models import EcommerceUsers
from converter.dbdata_to_json import DataConverter
from exceptions.usererror import EcommerceUserError


class UserSignInSerializer(DataConverter):
    Model = EcommerceUsers
    keys = ['email', 'password']
    UserDetails = ""

    @classmethod
    def validate_user(cls):
        if cls.Model_key['email'] == None or cls.Model_key['email'] == '':
            raise EcommerceUserError('Email field cannot be empty')
        if cls.Model_key['password'] == None or cls.Model_key['password'] == '':
            raise EcommerceUserError('Password field cannot be empty')
        

    @classmethod
    def login_user(cls):
        try:
            cls.validate_user()
        except EcommerceUserError as e:
            raise EcommerceUserError(message=repr(e))
        else:
            try:
                user = cls.Model.objects.raw(
                raw_query='select * from account_ecommerceusers where email = %s', 
                params=[cls.Model_key['email']]
                )
               
                for i in user:
                    if i.email == cls.Model_key['email']:
                        cls.UserDetails = i
                cls.UserDetails.check_password(cls.Model_key['password'])
            except:
                raise EcommerceUserError("User does not exit. Signup to login")
            else:
                access_token = cls.UserDetails.generate_access_token()
                refresh_token = cls.UserDetails.generate_refresh_token()
                return {
                    'firstname': cls.UserDetails.first_name,
                    'lastname': cls.UserDetails.last_name,
                    'email': cls.UserDetails.email,
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }



            