from apps.restaurantApp.models import Solicitud, Receta, Mesa, Inventario, Reserva
from faker import Faker
from ddf import G, N,F
import pytest

fake = Faker()
#Fixtures
@pytest.fixture
def create_Solicitud():
    return G(Solicitud)

@pytest.fixture
def create_receta():
    return G(Receta)

@pytest.fixture
def create_Mesa():
    return G(Mesa)

@pytest.fixture
def create_inventario():
    return G(Inventario)

@pytest.fixture
def create_reserva():
    return G(Reserva)

#Pruebas creacion modelos de restaurantApp

@pytest.mark.django_db #Solicitud
def test_create_Solicitud(create_Solicitud):
    create_Solicitud.save()
    assert create_Solicitud.estado == True

@pytest.mark.django_db #Receta
def test_create_receta(create_receta):
    create_receta.save()
    assert create_receta.disponible == True

@pytest.mark.django_db #Mesa
def test_create_mesa(create_Mesa):
    assert create_Mesa.disponible == True

@pytest.mark.django_db #Inventario
def test_create_inventario(create_inventario):
    print(create_inventario.nombre_encargado.nombres) #Prueba de relacion con el modelo Usuario
    assert create_inventario.disponibilidad_stock == True

@pytest.mark.django_db #Reserva
def test_create_reserva(create_reserva):
    print(create_reserva.mesa.nro_mesa) #Prueba de relacion con el modelo Mesa
    print(create_reserva.cliente.nombres) #Prueba de relacion con el modelo Usuario
    assert create_reserva.estado == True

