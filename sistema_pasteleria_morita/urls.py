"""
URL configuration for sistema_pasteleria_morita project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from carrito.views import carrito
from credenciales_clientes.views import credenciales, get_municipios
from cuenta.views import mi_cuenta
from gestion_categorias.views import gestion_categorias, nueva_categoria, eliminar_categoria, editar_categoria
from gestion_empleados.views import gestion_empleados, nuevo_empleado, \
    editar_empleado, eliminar_empleado
from gestion_presentacion.views import gestion_presentacion, nueva_presentacion, editar_presentacion, \
    eliminar_presentacion
from login.views import Ingreso
from menu_administracion.views import menu_admin
from menu_empleados.views import menu_empleado
from gestion_productos.views import gestion_productos, nuevo_producto, eliminar_producto, editar_producto
from nosotros.views import nosotros
from recuperacion_clave.views import recuperar_clave, cambiar_clave
from sistema_pasteleria_morita import settings
from django.contrib.auth import views as auth_views

from web_principal.views import web_principal
from web_productos.views import web_productos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loginEmp', Ingreso, name='LoginEmp'),
    path('principalAdmin', menu_admin, name='prinAdmins'),
    path('logout/', auth_views.LogoutView.as_view(next_page='LoginEmp'), name='logout'),
    path('principalEmp', menu_empleado, name='prinEmps'),
    path('gestionEmpleados', gestion_empleados, name='gestEmpleados'),
    path('agregarEmpleado', nuevo_empleado, name='nuevoEmpleado'),
    path('eliminarEmpleado/<int:id>', eliminar_empleado),
    path('editarEmpleado/<int:id>', editar_empleado),
    path('gestionProductos', gestion_productos, name='gestProductos'),
    path('agregarProductos', nuevo_producto, name='nuevoProducto'),
    path('eliminarProducto/<int:id>', eliminar_producto),
    path('editarProducto/<int:id>', editar_producto),
    path('gestion_categorias', gestion_categorias, name='gestCategorias'),
    path('agregarCategoria', nueva_categoria, name='nuevaCategoria'),
    path('editarCategoria/<int:id>', editar_categoria),
    path('eliminarCategoria/<int:id>', eliminar_categoria),
    path('gestion_presentacion', gestion_presentacion, name='gestPresentacion'),
    path('agregarPresentacion', nueva_presentacion, name='nuevaPresentacion'),
    path('editarPresentacion/<int:id>', editar_presentacion),
    path('eliminarPresentacion/<int:id>', eliminar_presentacion),

# URLS CLIENTES
    path('', web_principal, name='pagPrincipal'),
    path('productos', web_productos, name='pagProductos'),
    path('credenciales', credenciales, name='credenciales'),
    path('get_municipios/',get_municipios, name='get_municipios'),
    path('mi_cuenta',mi_cuenta, name='mi_cuenta'),
    path('nosotros', nosotros, name='nosotros'),
    path('carrito', carrito, name='carrito'),
    path('recuperarClave', recuperar_clave, name='recuperarClave'),
    path('CambiarClave/<str:token>/', cambiar_clave, name='CambiarClave'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
