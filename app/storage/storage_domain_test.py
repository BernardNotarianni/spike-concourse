import storage_domain

def test_storage_data():
    assert storage_domain.get_data() == "data in the storage"
