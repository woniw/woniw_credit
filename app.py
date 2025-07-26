# library imports
from flask import Flask, render_template, request, jsonify, url_for, redirect
import logging

from data.json_management import save_json
from data.variables import data

#! COLOR IMPORTS
from data.variables import bright_blue
from data.variables import red
from data.variables import green
from data.variables import bright_magenta

print(f"LOG: {data}")
app = Flask(__name__)

# FINISHED
@app.route('/', methods=["GET", "POST"])
def index():
    username = None
    password = None

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        print(f"{bright_blue}username: {username}")
        print(f"{bright_blue}password: {password}")

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

                data['current_login']["username"] = username
                data['current_login']["password"] = password
                save_json('data.json', data)
                return redirect(url_for("info_page"))
            elif password != data['users'][username]["important"]['password']:
                print(f"{red}-----------------------------")
                print(f"{red} password is incorrect!")
                print(f"{red}----------------------------")
                invalid_password_message = "Invalid Password"
                return render_template("index.html", invalid_password_message=invalid_password_message)
    return render_template('index.html')

@app.route('/info_page')
def info_page():
    username = data['current_login']['username']
    password = data['current_login']['password']

    user_balance_checking = data['users'][username]['balance_info']['checking']['balance']
    user_balance_monthly_fees = data['users'][username]['balance_info']['checking']['fees']
    user_balance_savings = data['users'][username]['balance_info']['savings']
    overdraft_fees = data['users'][username]['balance_info']['checking']['overdraft_fees']
    
    print("")
    print("")
    print(f"{bright_magenta}---- LOG ----")
    print(f"{bright_magenta}CHECKING: {user_balance_checking}")
    print(f"{bright_magenta}SAVINGS: {user_balance_savings}")
    print(f"{bright_magenta}SAVINGS: {user_balance_monthly_fees}")
    print(f"{bright_magenta}OVERDRAFT FEES: {overdraft_fees}")
    print("")
    print("")

    return render_template(
        "information_page.html",
        username=username,
        password=password,
        checking=user_balance_checking,
        savings=user_balance_savings,
        monthly_fees=user_balance_monthly_fees,
        overdraft=overdraft_fees
        )

if __name__ == "__main__":
    app.run(debug=True)
