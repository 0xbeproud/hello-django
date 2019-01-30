from django.urls import path

from api.views import CacheDetail, NoCacheDetail

urlpatterns = [

    path('cache', CacheDetail.as_view()),
    path('no-cache', NoCacheDetail.as_view()),

]
