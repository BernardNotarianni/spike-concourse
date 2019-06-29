
def backend_message(storage_connector):
    data = storage_connector.get_data()
    return "grabbed {} from storage".format(data)
