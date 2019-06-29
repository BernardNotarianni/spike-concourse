import frontend_domain

class MockBackendConnector:
    def get_message(self):
        return "I am the mock"

def test_frontend_message():
    connector = MockBackendConnector()
    assert frontend_domain.the_message(connector) == "backend said I am the mock"
