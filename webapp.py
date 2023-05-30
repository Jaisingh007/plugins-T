from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def start():
    return "NobiUb Started Successfully"

os.system("python3 -m TelethonNobi")
app.run(port=5000)