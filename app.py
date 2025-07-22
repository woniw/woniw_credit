# library imports
from flask import Flask, render_template, request, jsonify, url_for, redirect
import logging

from data.variables import data

#! COLOR IMPORTS
from data.variables import red
from data.variables import green

print(f"LOG: {data}")
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    username = None
    password = None

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        print(f"{red}username: {username}")
        print(f"{red}password: {password}")

        if username not in data['users']:
            print(f"{red}-----------------------------")
            print(f"{red} user does not exist")
            print(f"{red}----------------------------")
            invalid_username_message = "Invalid username"
            return render_template('index.html', invalid_username_message=invalid_username_message)
        elif username in data['users']:
            if password == data['users'][username]["important"]['password']:
                print(f"{green}-----------------------------")
                print(f"{green} password is correct!")
                print(f"{green}----------------------------")
            elif password != data['users'][username]["important"]['password']:
                print(f"{red}-----------------------------")
                print(f"{red} password is incorrect!")
                print(f"{red}----------------------------")
                invalid_password_message = "Invalid Password"
                return render_template("index.html", invalid_password_message=invalid_password_message)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
