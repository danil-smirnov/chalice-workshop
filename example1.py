from chalice import Chalice, NotFoundError

app = Chalice(app_name='Cloud9')

@app.route('/')
def index():
    print('Error!')
    raise NotFoundError('Nothing in this path!')
