from django.urls import path
from api_basic.views import *
from api_basic.Views.authentication import *
from api_basic.Views.product import *

urlpatterns = [
    path('article/', article_list),
    path('article/<int:pk>', article_detail),
    path('auth/login', loginAPIView),
    path('auth/register', registerAPIView),
    path('auth/me', getCurrentUser),
    path('product/', product_listAPIView),
]