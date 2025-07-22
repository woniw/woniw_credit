from flask import Flask, render_template, request, jsonify, url_for, redirect
from data.variables import data
import logging

print(f"LOG: {data}")
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    username = None
    password = None

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        from data.variables import red
        print(f"{red}username: {username}")
        print(f"{red}password: {password}")

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
