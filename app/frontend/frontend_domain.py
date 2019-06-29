
def the_message(backend_connector):
    data = backend_connector.get_message()
    return "backend said {}".format(data)
