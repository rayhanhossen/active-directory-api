import copy

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from components.helper.response_helper import ErrorResponse, SuccessResponse
from components.active_directory.user import UserManager
from api.serializers import ADUserSerializer


class UserProvision(APIView):
    def post(self, request):
        data = copy.deepcopy(request.data)
        try:
            serializer = ADUserSerializer(data=data)
            if serializer.is_valid():
                employee = serializer.save()
                user_principle, ad_response = UserManager().create_user(employee)
                if ad_response['result'] == 0:
                    # provisional employee status update
                    employee.status = 1
                    employee.save()
                    response = SuccessResponse(f"Provisioning of employee ({user_principle}) was successful!")
                    return Response(response.to_json(), status=status.HTTP_201_CREATED)
                else:
                    employee.delete()
                    response = ErrorResponse(
                        f"AD operation could not be performed. Error description: {ad_response['description']}")
                    return Response(response.to_json(), status=status.HTTP_400_BAD_REQUEST)
            else:
                response = ErrorResponse(f"Provisioning employee unsuccessful!", serializer.errors)
                return Response(response.to_json(), status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            response = ErrorResponse(str(e))
            return Response(response.to_json(), status=status.HTTP_400_BAD_REQUEST)
