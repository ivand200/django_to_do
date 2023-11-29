import pytest

from rest_framework.test import APIClient
from tasks.models import Task, Job


@pytest.mark.django_db
def test_create_task_no_user() -> None:
    """
    GIVEN Create a task without user
    WHEN POST "/api/tasks/"
    THEN return status_code == 401
    """
    task_data = {"title": "Pytest"}

    client = APIClient()
    r = client.post(path="/api/tasks/", data=task_data, format="json")
    
    assert r.status_code == 401


@pytest.mark.django_db
def test_create_task_by_user(create_auth_client, create_user) -> None:
    """
    GIVEN Create task by user
    WHEN POST "/api/tasks/"
    THEN return status_code == 201,
         check task title, user id, jobs in response
    """
    user = create_user(email="pytest@test.com")
    task_data = {"title": "Pytest"}

    auth_client = create_auth_client(user)
    r = auth_client.post(path="/api/tasks/", data=task_data, format="json")

    assert r.status_code == 201
    assert r.data["title"] == "Pytest"
    assert r.data["user"] == user.id
    assert r.data["jobs"] == []


@pytest.mark.django_db
def test_user_get_tasks(create_auth_client, create_user, create_task) -> None:
    """
    GIVEN User get his tasks
    WHEN GET "/api/tasks/"
    THEN return status_code == 200,
         check that only current user tasks in response
    """
    user = create_user(email="pytest@test.com")
    user_task = create_task(user)
    user_task = create_task(user)
    user_task = create_task(user)

    second_user = create_user(email="pytest@second.com")
    second_user_task = create_task(second_user)

    client = create_auth_client(user)
    r = client.get(path="/api/tasks/")
    user_tasks = [task for task in r.data if task["user"] == user.id]
    second_user_tasks = [task for task in r.data if task["user"] == second_user.id]
    
    assert r.status_code == 200
    assert len(user_tasks) == 3
    assert len(second_user_tasks) == 0


@pytest.mark.django_db
def test_user_update_task_title(create_auth_client, create_user, create_task) -> None:
    """
    GIVEN Current user update his task
    WHEN PATCH "/api/tasks/"
    THEN return status_code == 200
         check updated task title, user id in response
    """
    user = create_user(email="pytest@mail.com")
    task = create_task(user)

    payload = {"title": "Updated title"}
    client = create_auth_client(user)
    r = client.patch(path=f"/api/tasks/{task.id}/", data=payload, format="json")

    assert r.status_code == 200
    assert r.data["title"] == payload["title"]
    assert r.data["user"] == user.id


@pytest.mark.django_db
def test_user_delete_task(create_auth_client, create_user, create_task) -> None:
    """
    GIVEN Current user delete his task
    WHEN DELETE "/api/tasks/"
    THEN return status_code == 204
    """
    user = create_user(email="pytest@test.com")
    user_task = create_task(user=user, title="Task to delete")

    client = create_auth_client(user)
    r = client.delete(path=f"/api/tasks/{user_task.id}/")

    task_db = Task.objects.filter(id=user_task.id).first()
    
    assert r.status_code == 204
    assert task_db is None


@pytest.mark.django_db
def test_user_delete_another_user_task(create_auth_client, create_user, create_task) -> None:
    """
    GIVEN User try to delete another user task
    WHEN DELETE "/api/tasks/"
    THEN return status_cdoe == 404
    """
    user = create_user(email="pytest@test.com")
    user_task = create_task(user=user, title="Task to delete")
    second_user = create_user(email="second@user.com")

    client = create_auth_client(second_user)
    r = client.delete(path=f"/api/tasks/{user_task.id}/")

    assert r.status_code == 404



@pytest.mark.django_db
def test_user_update_another_user_task(create_auth_client, create_task, create_user) -> None:
    """
    GIVEN Current user try update another user task
    WHEN PATCH "/api/tasks/"
    THEN return status_code == 404
    """
    user = create_user(email="pytest@test.com")
    user_task = create_task(user)

    second_user = create_user(email="second@user.com")
    second_user_task = create_task(user=user, title="Second user task")

    payload = {"title": "Just update"}
    client = create_auth_client(second_user)
    r = client.patch(path=f"/api/tasks/{user_task.id}/", data=payload, format="json")
    
    assert r.status_code == 404


@pytest.mark.django_db
def test_user_get_another_user_task(create_auth_client, create_user, create_task) -> None:
    """
    GIVEN User get another user task
    WHEN GET "/api/tasks/"
    THEN return status_code == 404
    """
    user = create_user(email="pytest@test.com")
    user_task = create_task(user)

    second_user = create_user(email="second@user.com")
    second_user_task = create_task(user=user, title="second user task")

    client = create_auth_client(second_user)
    r = client.get(path=f"/api/tasks/{user_task.id}/")

    assert r.status_code == 404


@pytest.mark.django_db
def test_user_create_job() -> None:
    """
    GIVEN
    WHEN
    THEN
    """


@pytest.mark.django_db
def test_user_update_job() -> None:
    """
    GIVEN
    WHEN
    THEN
    """


@pytest.mark.django_db
def test_user_get_task_with_jobs() -> None:
    """
    GIVEN
    WHEN
    THEN
    """


@pytest.mark.django_db
def test_create_task_by_user_with_jobs():
    """
    GIVEN
    WHEN
    THEN
    """



# @pytest.mark.django_db
# def test_user_create_another(create_auth_client, create_user, create_task) -> None:
#     """
#     GIVEN
#     WHEN
#     THEN
#     """
#     user = create_user(email="pytest@test.com")
#     user_task = create_task(user)

#     new_task = {"title": "New Task!"}

#     client = create_auth_client(user)
#     r = client.post(path="/api/tasks/", data=new_task, format="json")
#     print(r.data)
