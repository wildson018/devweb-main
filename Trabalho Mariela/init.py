from flask import Flask, render_template, request, redirect, url_for, flash
app_Wildson = Flask (__name__)

app_Wildson.secret_key = "secretkey"  # Necessário para mensagens flash

@app_Wildson.route("/")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app_Wildson.run(debug=True)
