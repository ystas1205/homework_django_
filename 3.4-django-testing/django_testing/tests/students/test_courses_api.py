import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Student, Course


base_url = "/api/v1/courses/"


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_student_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def course(course_student_factory):
    return course_student_factory(_quantity=10)


@pytest.fixture
def student(course_student_factory):
    return course_student_factory(_quantity=20)

 # проверка получения первого курcа


@pytest.mark.django_db
def test_retrieve_course(client, course):
    # Arrange
    # Act
    response = client.get(f"{base_url}{course[0].id}/")
    print(course[0].id)
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == course[0].id


# проверка получения списка курсов
@pytest.mark.django_db
def test_list_course(client, course):
    # Arrange
    # Act
    response = client.get(base_url)
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(course)


# проверка фильтрации списка курсов по `id`
@pytest.mark.django_db
def test_filter_cource_id(client, course):
    # Arrange
    # Act
    response = client.get(f"{base_url}?id={course[1].id}")
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == course[1].id


# проверка фильтрации списка курсов по `name`
@pytest.mark.django_db
def test_filter_course_name(client, course):
    # Arrange
    # Act
    response = client.get(f"{base_url}?name={course[2].name}")
    # Assert
    print(course)
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == course[2].name


# тест успешного создания курса
@pytest.mark.django_db
def test_create_course(client):
    # Arrange
    count = Course.objects.count()
    # Act
    response = client.post(f"{base_url}", data={'name': 'test'})
    # Assert
    assert response.status_code == 201
    assert Course.objects.count() == count+1


# тест успешного обновления курса
@pytest.mark.django_db
def test_update_course(client, course):
    # Arrange
    # Act
    response = client.patch(
        f"{base_url}{course[1].id}/", data={'name': 'test'})
    data = response.json()
    # Assert
    assert response.status_code == 200
    assert data['name'] == 'test'


# тест успешного удаления курса
@pytest.mark.django_db
def test_delete_course(client, course):
    # Arrange
    count = Course.objects.count()
    # Act
    response = client.delete(f"{base_url}{course[0].id}/")
    # Assert
    assert response.status_code == 204
    assert Course.objects.count() == count - 1

