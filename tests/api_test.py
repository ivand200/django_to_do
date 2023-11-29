import pytest
from rest_framework.test import APIClient
from users.models import CustomUser


@pytest.mark.django_db
def test_create_user_model() -> None:
    """
    GIVEN
    WHEN
    THEN
    """
    user = CustomUser(email="test@mail.com", password="t3stP@assw0r!", username="pytest test")
    print(user.date_joined)

    assert user.email == "test@mail.com"
    assert user.password == "t3stP@assw0r!"
    assert user.username == "pytest test"
    assert user.date_joined is not None


@pytest.mark.django_db
def test_user_registration():
    """
    GIVEN
    WHEN
    THEN
    """
    user_data = {"email": "pytest@test.com", "password": "S0m3password1", "username": "new_test_user"}
    client = APIClient()
    r = client.post(path="/api/register/", data=user_data, format="json")

    assert r.status_code == 201
    assert r.data["email"] == user_data["email"]
    assert r.data["username"] == user_data["username"]
