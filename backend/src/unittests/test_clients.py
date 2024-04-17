from datetime import datetime
from unittest import TestCase

from backend.src.api.core.models import Client
from backend.src.api.core.models.clients import ClientStatus


class TestClientModel(TestCase):
    def test_attributes(self):
        # Check that the attributes of the class are defined correctly
        self.assertTrue(hasattr(Client, "account_number"))
        self.assertTrue(hasattr(Client, "name"))
        self.assertTrue(hasattr(Client, "surname"))
        self.assertTrue(hasattr(Client, "second_name"))
        self.assertTrue(hasattr(Client, "birthday"))
        self.assertTrue(hasattr(Client, "TIN"))
        self.assertTrue(hasattr(Client, "responsible_person_full_name"))
        self.assertTrue(hasattr(Client, "status"))

    def test_attributes_status(self):
        # Check that the default status of the client is 'NOT_AT_WORK'
        client = Client(
            account_number=123,
            name="John",
            surname="Doe",
            second_name="Smith",
            birthday=datetime(1990, 5, 15),
            TIN="123456789012",
            responsible_person_full_name="Jane Doe",
        )

    def test_attributes_values(self):
        # Check each field of the Client object for the expected values
        client = Client(
            account_number=123,
            name="John",
            surname="Doe",
            second_name="Smith",
            birthday=datetime(1990, 5, 15),
            TIN="123456789012",
            responsible_person_full_name="Jane Doe",
        )
        self.assertEqual(client.account_number, 123)
        self.assertEqual(client.name, "John")
        self.assertEqual(client.surname, "Doe")
        self.assertEqual(client.second_name, "Smith")
        self.assertEqual(client.birthday, datetime(1990, 5, 15))
        self.assertEqual(client.TIN, "123456789012")
        self.assertEqual(client.responsible_person_full_name, "Jane Doe")
