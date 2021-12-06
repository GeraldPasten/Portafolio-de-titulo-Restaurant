from django.urls import path
from .views import *
from . import views
from django.views.generic import TemplateView
from apps.restaurantApp.views import InicioMesa,ListadoMesa, CrearMesa, ActualizarMesa,EliminarMesa
from apps.restaurantApp.views import InicioInventario, ListadoInventario, CrearInventario, ActualizarInventario, EliminarInventario
from apps.restaurantApp.views import InicioSolicitud, CrearSolicitud, ListadoSolicitud, ActualizarSolicitud, EliminarSolicitud
from apps.restaurantApp.views import InicioReserva, RegistrarReserva,ListadoReserva, ActualizarReserva, EliminarReserva
from apps.restaurantApp.views import InicioReceta, ListadoReceta, CrearReceta, ActualizarReceta, EliminarReceta
from apps.restaurantApp.views import agregar_producto, eliminar_producto, restar_producto, limpiar_carrito

urlpatterns = [
    # Modelo Mesa
    path('inicio_mesa/',InicioMesa.as_view(), name = 'inicio_mesa'),
    path('listado_mesa/', ListadoMesa.as_view(), name = 'listado_mesa'),
    path('crear_mesa/',CrearMesa.as_view(), name = 'crear_mesa'),
    path('editar_mesa/<int:pk>/', ActualizarMesa.as_view(), name = 'editar_mesa'),
    path('eliminar_mesa/<int:pk>/', EliminarMesa.as_view(), name = 'eliminar_mesa'),
    path('listado_mesa_disponibles/',ListadoMesaDisponibles.as_view(), name = 'listado_mesa_disponibles'),
    #Modelo Inventario
    path('inicio_inventario/',InicioInventario.as_view(), name = 'inicio_inventario'),
    path('listado_inventario/', ListadoInventario.as_view(), name = 'listado_inventario'),
    path('crear_inventario/',CrearInventario.as_view(), name = 'crear_inventario'),
    path('editar_inventario/<int:pk>/', ActualizarInventario.as_view(), name = 'editar_inventario'),
    path('eliminar_inventario/<int:pk>/', EliminarInventario.as_view(), name = 'eliminar_inventario'),
    #Solicitud
    path('Inicio_solicitud/',InicioSolicitud.as_view(), name = 'inicio_solicitud'),
    path('listado_solicitud/',ListadoSolicitud.as_view(), name = 'listado_solicitud'),
    path('crear_solicitud/',CrearSolicitud.as_view(), name = 'crear_solicitud'),
    path('editar_solicitud/<int:pk>/',ActualizarSolicitud.as_view(), name = 'editar_solicitud'),
    path('eliminar_solicitud/<int:pk>/',EliminarSolicitud.as_view(), name= 'eliminar_solicitud'),

    # Reserva
    path('inicio_reserva/', InicioReserva.as_view(), name= 'inicio_reserva'),
    path('listado_reserva/', ListadoReserva.as_view(), name = 'listado_reserva'),
    path('registrar_reserva/', RegistrarReserva.as_view(),name ='registrar_reserva'),
    path('editar_reserva/<int:pk>/', ActualizarReserva.as_view(), name='editar_reserva'),
    path('eliminar_reserva/<int:pk>/', EliminarReserva.as_view(), name='eliminar_reserva'),
    # Receta
    path('inicio_receta/', InicioReceta.as_view(), name= 'inicio_receta'),
    path('listado_receta/', ListadoReceta.as_view(), name = 'listado_receta'),
    path('crear_receta/', CrearReceta.as_view(),name ='registrar_receta'),
    path('editar_receta/<int:pk>/', ActualizarReceta.as_view(), name='editar_receta'),
    path('eliminar_receta/<int:pk>/', EliminarReceta.as_view(), name='eliminar_receta'),
    path('listado-recetas-disponibles/',ListadoRecetasDisponibles.as_view(), name = 'listado_receta_disponibles'),
    path('detalle-receta/<int:pk>/', DetalleRecetaDiponible.as_view(), name = 'detalle_receta'),
    #Orden
    path('inicio_orden/', InicioOrden.as_view(), name= 'inicio_orden'),
    path('listado_orden/', ListadoOrden.as_view(), name = 'listado_orden'),
    path('crear_orden/', CrearOrden.as_view(),name ='crear_orden'),
    path('editar_orden/<int:pk>/', ActualizarOrden.as_view(), name='editar_Orden'),
    path('eliminar_orden/<int:pk>/', EliminarOrden.as_view(), name='eliminar_Orden'),
    # Carrito
    path('agregar/<int:receta_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:receta_id>/', eliminar_producto, name="Del"),
    path('restar/<int:receta_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('guadar/',guardar_carrito, name='guardar'),
    #Boleta
    path('inicio_cart/',views.InicioCart.as_view(),name="inicio-carrito"),
    path('inicio_order/',views.InicioOrder.as_view(),name="inicio-order"),
    path('boleta/',boleta,name= 'boleta'),
    # Orden- carrito2.0
    path("cart", views.cart, name="cart"),
    path("checkout", views.checkout, name="checkout"),
    path("view-orders/", views.view_orders, name="view_orders"),
    path("mark_order_as_delivered", views.mark_order_as_delivered, name="mark_order_as_delivered"),
    path("save_cart", views.save_cart, name="save_cart"),
    path("retrieve_saved_cart", views.retrieve_saved_cart, name="retrieve_saved_cart"),
    path("check_superuser", views.check_superuser, name="check_superuser"),

]
