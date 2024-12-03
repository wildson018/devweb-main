from flask import Flask, render_template, request, redirect, url_for, flash
app_Wildson = Flask (__name__)

app_Wildson.secret_key = "secretkey" 

usuarios = {
    'usuario@example.com': {'senha': 'senha123'},  
}

@app_Wildson.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("password")

        if email in usuarios:
            if usuarios[email]['senha'] == senha:
                flash("Login realizado com sucesso!", "success")
                return redirect(url_for("login")) 
            else:
                flash("Senha incorreta. Tente novamente.", "error")
        else:
            flash("E-mail não encontrado. Tente novamente.", "error")

        return redirect(url_for("login"))

    return render_template("login.html")


if __name__ == "__main__":
    app_Wildson.run(debug=True)
