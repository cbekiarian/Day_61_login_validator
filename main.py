from flask import Flask, render_template
from forms import RegistrationForm
from flask_bootstrap import Bootstrap4

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
bootstrap = Bootstrap4(app)
app.secret_key = "some secret string"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.email.data =="admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)
if __name__ == '__main__':
    app.run(debug=True)
