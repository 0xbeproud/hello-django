from django.urls import path, include

urlpatterns = [
    path('users/', include("api.users.urls")),
    path('demo/', include("api.demo.urls")),
    # path('logging', LoggingDetail.as_view()),
]
