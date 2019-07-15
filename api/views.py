# Create your views here.
import logging

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

logger = logging.getLogger(__name__)


class LoggingDetail(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        logger.info("logging info")
        logger.debug("logging debug")
        logger.error("logging error")
        return Response(data='logging test')


class Throttle(APIView):
    throttle_classes = (UserRateThrottle,)

    def get(self, request):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
