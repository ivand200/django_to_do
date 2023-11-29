import pytest

from rest_framework.test import APIClient

from users.models import CustomUser
from tasks.models import Task, Job


@pytest.fixture(scope="function")
def create_auth_client():

    def _create_auth_client(user):
        client = APIClient()
        client.force_authenticate(user=user)

        return client
    
    return _create_auth_client


@pytest.fixture(scope="function")
def create_user():

    def _create_user(email: str):
        return CustomUser.objects.create_user(
            email=email,
            password="S0mepa@55word!",
            username="Test user"
        )

    return _create_user


@pytest.fixture(scope="function")
def create_task():

    def _create_task(user: CustomUser, title: str = "Test task"):
        return Task.objects.create(
            title=title,
            user=user
        )
    
    return _create_task


@pytest.fixture(scope="function")
def create_job():

    def _create_job(task: Task):
        return Job.objects.create(
            title="Test job",
            description="Test description",
            task=task
        )

    return _create_job