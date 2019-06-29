import backend_domain

class MockStorageConnector:
    def get_data(self):
        return "I am the mock"


def test_backend_message():
    connector = MockStorageConnector()

    assert backend_domain.backend_message(connector) == "grabbed I am the mock from storage"
