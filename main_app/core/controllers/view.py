from main import app


@app.get("/")
def index():
    return 'main page'
