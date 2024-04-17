from pathlib import Path
from unittest import TestCase

from backend.src.api.core.config import Settings


class TestSettings(TestCase):
    def setUp(self):
        self.settings = Settings()

    def test_api_v1_prefix_default_value(self):
        self.assertEqual(self.settings.api_v1_prefix, "/api/v1")

    def test_db_default_values(self):
        self.assertEqual(
            self.settings.db.db_url,
            "postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres",
        )
        self.assertFalse(self.settings.db.db_echo)
        self.assertEqual(self.settings.db.db_engine, "postgres")

    def test_auth_jwt_default_values(self):
        self.assertEqual(
            self.settings.auth_jwt.private_key_path,
            Path(__file__).parent.parent.parent / "certs" / "jwt-private.pem",
        )
        self.assertEqual(
            self.settings.auth_jwt.public_key_path,
            Path(__file__).parent.parent.parent / "certs" / "jwt-public.pem",
        )
        self.assertEqual(
            self.settings.auth_jwt.REFRESH_TOKEN_EXPIRES_MINUTES, 60 * 24 * 7
        )
        self.assertEqual(self.settings.auth_jwt.ACCESS_TOKEN_EXPIRES_MINUTES, 5)
        self.assertEqual(self.settings.auth_jwt.JWT_ALGORITHM, "RS256")
        self.assertEqual(self.settings.auth_jwt.TOKEN_EXPIRES_MINUTES, 2)
        self.assertEqual(self.settings.auth_jwt.TOKEN_URLSAFE_LEN, 32)
        self.assertEqual(self.settings.auth_jwt.token_type.ACCESS, "access")
        self.assertEqual(self.settings.auth_jwt.token_type.REFRESH, "refresh")

    def test_client_origin_default_value(self):
        self.assertEqual(self.settings.CLIENT_ORIGIN, "http://localhost:8000")
