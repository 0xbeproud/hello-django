from django.urls import path

from api.demo import views

urlpatterns = [
    path("demo/", views.DemoListAPIView.as_view()),
    path("exception/", views.ExceptionDetailAPIView.as_view()),
    path("cache/", views.CacheDetailAPIView.as_view()),
    path("nocache/", views.NoCacheDetailAPIView.as_view()),
    path("throttles/", views.ThrottleAPIView.as_view()),
]
