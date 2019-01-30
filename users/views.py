import logging

import requests
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from djangoapi.settings import CLIENT_ID, CLIENT_SECRET
from users.serializers import CreateUserSerializer

logger = logging.getLogger(__name__)


@swagger_auto_schema(method='POST', operation_summary="사용자 등록", operation_description="사용자 등록시 token 발급")
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        r = requests.post('http://127.0.0.1:8000/o/token/',
                          data={
                              'grant_type': 'password',
                              'username': request.data['username'],
                              'password': request.data['password'],
                              'client_id': CLIENT_ID,
                              'client_secret': CLIENT_SECRET,
                          },
                          )

        return Response(r.json())
    return Response(serializer.errors)


@swagger_auto_schema(method='POST', operation_summary="token 발급", operation_description="토큰 발급 요청")
@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    r = requests.post(
        'http://127.0.0.1:8000/o/token/',
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@swagger_auto_schema(method='POST', operation_summary="token 갱신")
@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    r = requests.post(
        'http://127.0.0.1:8000/o/token/',
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@swagger_auto_schema(method='POST', operation_summary="token 삭제")
@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    r = requests.post(
        'http://127.0.0.1:8000/o/revoke_token/',
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    return Response(r.json(), r.status_code)
