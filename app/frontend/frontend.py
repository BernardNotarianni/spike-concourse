from bottle import route, run, template
import frontend_domain

@route('/')
def index():
    message = frontend_domain.my_message()
    return '<html><h1>Welcome to master branch</h1><p>{}</p></html>'.format(message)

run(host='0.0.0.0', port=8000)

