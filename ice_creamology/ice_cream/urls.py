from django.urls import path

from . import views


urlpatterns = [
    # Main page
    path('', views.index),
    # Ice cream list
    path('ice_cream/', views.ice_cream_list),
    # More information about ice cream. We are waiting for a variable of int type,
    # and will use it under the name pk
    path(
        'ice_cream/<int:pk>/',
        views.ice_cream_detail
    ),
]
