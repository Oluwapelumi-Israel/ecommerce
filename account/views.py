import datetime
from jwt import ExpiredSignatureError, InvalidSignatureError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from converter.getdata import GetData
from converter.signup import UserSerialiser
from converter.signin import UserSignInSerializer
from exceptions.usererror import EcommerceUserError
# Create your views here.

@api_view(['POST'])
def signUpPage(request: Request):
    try:
        UserSerialiser.getDataToDbFromJson(jsonData=request.data)
        details = UserSerialiser.save()
        print(details)
    except EcommerceUserError as e:
        return Response(data={"message":repr(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response(data={"message":"working fine"}, status=status.HTTP_201_CREATED)



@api_view(['POST'])
def loginUpPage(request: Request):
    try:
        UserSignInSerializer.getDataToDbFromJson(jsonData=request.data)
        result = UserSignInSerializer.login_user()
    except EcommerceUserError as e:
        return Response(data={"message":repr(e)}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response(data=result, status=status.HTTP_202_ACCEPTED)
       
        

@api_view(['POST'])
def getData(request: Request):
    try:
        GetData.getDataToDbFromJson(jsonData=request.data)
        user = GetData.decode_access_token()
        if user:
            return Response(data=user, status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        return Response(data={"message": repr(e.args).strip("(),''")}, status=status.HTTP_401_UNAUTHORIZED)
    
