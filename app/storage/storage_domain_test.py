import storage_domain

def test_storage_message():
    assert storage_domain.storage_message() == "Hello Concourse!"
