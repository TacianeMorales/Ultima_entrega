from django.urls import path
from produtos.models import Category

from produtos.views import (
    index, ola,
    CreateCategoryView,
    ListCategoryView,
    DetailCategoryView,
    UpdateCategoryView,
    DeleteCategoryView,
    teste,
    CreatInfosProdutView,
    ListInfosProdutView,
)

urlpatterns = [
    path('teste/', teste, name='teste'),
    path('', index.as_view(), name="index"),
    path('ola/', ola , name="ola"),
    path('category/add',
            CreateCategoryView.as_view(),
            name='create_category',
        ),
    path('category',
            ListCategoryView.as_view(),
            name='list_category',
        ),
    path('category/<int:pk>',
            DetailCategoryView.as_view(),
            name='category_detail'),
    path('category/<int:pk/update',
    UpdateCategoryView.as_view(),
    name='category_update'),
    path('category/<int:pk>/delete',
            DeleteCategoryView.as_view(),
            name='category_delete'),
    path('CreatProdutInfo/', CreatInfosProdutView.as_view(),
    name='CreatProdutInfo/'),
    path('ListInfosProdut/', ListInfosProdutView.as_view(),
    name='ListInfosProdut/'),

]