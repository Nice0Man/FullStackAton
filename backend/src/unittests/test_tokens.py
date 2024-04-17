from unittest import TestCase
from datetime import datetime
from uuid import UUID

from backend.src.api.core.models.tokens import Token


class TestTokenModel(TestCase):
    def test_attributes(self):
        # Проверяем, что атрибуты класса определены корректно
        self.assertTrue(hasattr(Token, "refresh_token"))
        self.assertTrue(hasattr(Token, "ua"))
        self.assertTrue(hasattr(Token, "ip"))
        self.assertTrue(hasattr(Token, "expires_in"))
        self.assertTrue(hasattr(Token, "created_at"))
        self.assertTrue(hasattr(Token, "updated_at"))

    def test_attributes_types(self):
        self.assertEqual(UUID, Token.refresh_token.type.python_type)
        self.assertEqual(str, Token.ua.type.python_type)
        self.assertEqual(str, Token.ip.type.python_type)
        self.assertEqual(int, Token.expires_in.type.python_type)
        self.assertEqual(datetime, Token.created_at.type.python_type)
        self.assertEqual(datetime, Token.updated_at.type.python_type)
