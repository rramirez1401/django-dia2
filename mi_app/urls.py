
from django.urls import path
from .views import (
    hola,
    ProductoCreateView,
    ProductoDeleteView,
    ProductoListView,
    ProductoUpdateView,
    ProductoDetailView)

""" urlpatterns = [
        path("",hola,name="hola"),
        path("productos/", listar_productos,name="lista_productos")
]
 """

urlpatterns = [
    path("", ProductoListView.as_view(),name="lista_productos"),
    path("crear/", ProductoCreateView.as_view(),name="crear_productos"),
    path("producto/<int:pk>", ProductoDetailView.as_view(),name="detail_productos"),
    path("producto/actualizacion/<int:pk>", ProductoUpdateView.as_view(),name="update_productos"),
    path("producto/borrar/<int:pk>", ProductoDeleteView.as_view(),name="borrar_productos")
]