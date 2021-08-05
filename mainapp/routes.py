from mainapp import app

@app.route('/')
@app.route('/index')
def index():
    return "Testing 1 2 3"