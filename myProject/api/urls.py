from django.urls import path
from . import views


# urlpattern for our api app.

urlpatterns = [
    path('product-status/', views.productStatus)
        ]
