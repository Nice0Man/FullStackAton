from typing import List
from unittest import TestCase


from backend.src.api.core.models.clients import Client
from backend.src.api.core.models.users import User


class TestUserModel(TestCase):
    def test_attributes(self):
        # Проверяем, что атрибуты класса определены корректно
        self.assertTrue(hasattr(User, "full_name"))
        self.assertTrue(hasattr(User, "login"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "clients"))

    def test_attributes_types(self):
        self.assertTrue(str, User.full_name.type.python_type)
        self.assertTrue(str, User.login.type.python_type)
        self.assertTrue(bytes, User.password.type.python_type)
        self.assertTrue(List[Client], User.clients)

    def test_str_representation(self):
        # Создаем экземпляр класса User
        user = User(full_name="John Doe", login="johndoe", password=b"password123")

        # Проверяем, что метод __str__ возвращает корректную строку
        expected_str = "User(id=None, username='John Doe')"
        self.assertEqual(str(user), expected_str)

    def test_repr_representation(self):
        # Создаем экземпляр класса User
        user = User(full_name="John Doe", login="johndoe", password=b"password123")

        # Проверяем, что метод __repr__ возвращает корректную строку
        expected_repr = "User(id=None, username='John Doe')"
        self.assertEqual(repr(user), expected_repr)
