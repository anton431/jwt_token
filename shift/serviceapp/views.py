from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from serviceapp.models import Person
from serviceapp.serializer import TokenSerializer
import requests


class PersonInfoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        username = request.user.username
        pers = Person.objects.filter(login = username).first()
        content = {'username': username,
                   'salary': pers.salary,
                   'date_up': pers.date_up}
        return Response(content)

class TokenView(APIView):
    serializer_class = TokenSerializer

    def post(self,request):
        token = request.data['token']
        header = {
            "Authorization": "Bearer {}".format(token),
            "Content-Type": "application/json",
        }
        response = requests.get(
            url=f'http://127.0.0.1:8000/person/',
            headers=header,
            timeout=5
        ).json()
        return Response(response)

