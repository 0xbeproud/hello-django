# Create your views here.
import time

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView


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
