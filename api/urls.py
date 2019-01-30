from django.urls import path

from api.views import CacheDetail, NoCacheDetail

urlpatterns = [

    path('cache', CacheDetail.as_view()),
    path('no-cache', NoCacheDetail.as_view()),
    # path('dapps/<int:dappid>/wallets', DappWalletList.as_view()),
    # path('dapps/<int:dappid>/wallets/<str:address>', DappWalletDetail.as_view()),
    # path('dapps/<int:dappid>/transactions', DappTransaction.as_view()),
    # path('dapps/<int:dappid>/wallets/<str:address>/transactions', DappWalletTransaction.as_view()),

]
