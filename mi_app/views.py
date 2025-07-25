from django.shortcuts import render 
from .models import Producto
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
# aqui se hacen los controladores


def hola(request):
    return render(request, "hola.html")

""" def listar_productos(request):
    productos = Producto.objects.all()   ##esto es la query##
                                                        ##{contexto}##
    return render(request, "lista_de_productos.html",{"productos":productos}) """

class ProductoListView(ListView):
    model = Producto
    template_name = "productos/producto_list.html"
    context_object_name = "productos"

class ProductoDetailView(DetailView):
    model = Producto
    template_name = "productos/producto_detail.html"
    context_object_name = "producto"

class ProductoCreateView(CreateView):
    model = Producto
    template_name = "productos/producto_form.html"
    fields = ["nombre", "descripcion", "precio", "stock", "imagen"]
    success_url = reverse_lazy("lista_productos")

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "productos/producto_form.html"
    fields = ["nombre", "descripcion", "precio", "stock", "imagen"]
    success_url = reverse_lazy("lista_productos")

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "productos/producto_confirm.html"
    success_url = reverse_lazy("lista_productos")