from django.urls import path

from api.views import CacheDetail, NoCacheDetail, LoggingDetail, DemoList, ExceptionDetail

urlpatterns = [

    path('logging', LoggingDetail.as_view()),
    path('cache', CacheDetail.as_view()),
    path('no-cache', NoCacheDetail.as_view()),
    path('demo', DemoList.as_view()),
    path('exception', ExceptionDetail.as_view()),
]
