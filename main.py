from flask import Flask


import os
app = Flask(__name__)
@app.get("/")
def home():
    output = "This is {} server: {}".format(os.getenv("ENV"),os.getenv("VER"))
    return output

app.run()