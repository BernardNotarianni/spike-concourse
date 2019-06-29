import backend_domain

def test_backend_message():
    assert backend_domain.my_message() == "Hello Concourse!"
