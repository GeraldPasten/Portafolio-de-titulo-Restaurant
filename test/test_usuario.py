from apps.usuario.models import Usuario, Rol
from faker import Faker
from ddf import G, N,F
import pytest

fake = Faker()

@pytest.mark.django_db
@pytest.fixture
def user_creation():
        rol = G(Rol)
        return N(Usuario, rol=rol)


#Pruebas sin fallos
@pytest.mark.django_db

def test_creacion_usuario(user_creation):
        print(user_creation.rol)
        user_creation.is_staff = False
        user_creation.save()
        assert user_creation.is_staff == False


@pytest.mark.django_db
def test_staff_usuario(user_creation):
        user_creation.is_staff = True
        user_creation.save()
        assert  user_creation.is_staff 


@pytest.mark.django_db
def test_creacion_susperuser(user_creation):
        user_creation.is_superuser = True
        user_creation.save()
        assert user_creation.is_superuser

#Pruebas con fallos
@pytest.mark.django_db
def test_creacion_usuario_fail():
        with pytest.raises(Exception):
                Usuario.objects.create_user(
                        password ='admin',
                        is_staff = False
                )


@pytest.mark.django_db
def test_staff_usuario_fail():
        with pytest.raises(Exception):
                Usuario.objects.creater_user(
                        password='admin',
                        is_staff = False
                )

@pytest.mark.django_db
def test_creacion_superuser():
        with pytest.raises(Exception):
                Usuario.objects.creatersuperuser(
                        password='admin',
                        is_superuser = False

                )



