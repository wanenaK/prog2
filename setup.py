from flask import Flask , render_templat
from modelo import pessoas
app = Flask (__name__)
@app.rounte("/")

def inicio ():
    return render_template ("inicio.html")

@app.router()