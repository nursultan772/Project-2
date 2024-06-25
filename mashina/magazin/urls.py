from django.urls import path, include
from .views import *

urlpatterns = [

    path('accounts/', include('allauth.urls')),

    path('user_profiles/', UserProfileViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='user_profile_list'),
    path('user_profile/<int:pk>/', UserProfileViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='user_profile_detail'),

    path('categories/', CategoryViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='category_list'),
    path('categories/<int:pk>/', CategoryViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category_detail'),

    path('products/', ProductViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='product_list'),
    path('products/<int:pk>/', ProductViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='product_detail'),

    path('car_photos/', CarPhotosViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='car_photos_list'),
    path('car_photos/<int:pk>/', CarPhotosViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='car_photos_detail'),

    path('favorites/', FavoriteViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='favorite_list'),
    path('favorites/<int:pk>/', FavoriteViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='favorite_detail'),

    path('baskets/', BasketViewSets.as_view({'get': 'list', 'post': 'create'}),
         name='basket_list'),
    path('baskets/<int:pk>/', BasketViewSets.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='basket_detail'),
]