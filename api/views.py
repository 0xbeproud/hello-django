# Create your views here.
import logging
import time

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

from api.exceptions import UserDoesNotExistException
from api.models import Demo
from api.serializers import DemoResponseSerializer, CreateDemoRequestSerializer

logger = logging.getLogger(__name__)


class LoggingDetail(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        logger.info("logging info")
        logger.debug("logging debug")
        logger.error("logging error")
        return Response(data='logging test')


class CacheDetail(APIView):
    permission_classes = [AllowAny, ]

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request):
        time.sleep(2)
        return Response(data="ok with cache")


class NoCacheDetail(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        time.sleep(2)
        return Response(data="ok with no cache")


class Throttle(APIView):
    throttle_classes = (UserRateThrottle,)

    def get(self, request):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)


class ExceptionDetail(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        raise UserDoesNotExistException(1)


class DemoList(APIView):
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(operation_summary="demo list 조회",
                         responses={
                             200: DemoResponseSerializer(many=True),
                         })
    def get(self, request):
        demos = Demo.objects.all()
        return Response(DemoResponseSerializer(demos, many=True).data)

    @swagger_auto_schema(operation_summary="application 생성",
                         request_body=CreateDemoRequestSerializer,
                         responses={
                             201: DemoResponseSerializer,
                             400: "Bad Request"
                         })
    def post(self, request):
        serializer = CreateDemoRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
