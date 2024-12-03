from flask import Flask, render_template, request, redirect, url_for, flash
app_Wildson = Flask (__name__)

app_Wildson.secret_key = "secretkey" 

@app_Wildson.route("/")
def login():
    return render_template("login.html")

@app_Wildson.route("/cadastro", methods=["GET", "POST"])


@app_Wildson.route("/register", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        name = request.form.get("name")
        cpf = request.form.get("cpf")
        email = request.form.get("email")
        phone = request.form.get("phone")
        address = request.form.get("address")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

       
        if password != confirm_password:
            flash("As senhas não coincidem. Tente novamente!", "error")
            return redirect(url_for("register"))

       
        flash("Cadastro realizado com sucesso!", "success")

    return render_template("cadastro.html")

if __name__ == "__main__":
    app_Wildson.run(debug=True)
