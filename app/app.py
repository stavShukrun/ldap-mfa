import os
from crypt import methods
from flask import Flask, flash, render_template, request, redirect, url_for
from form import *
from ldap_authentication import *
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
import pyotp


app = Flask(__name__,template_folder="./templates")

bootstrap = Bootstrap(app)
app.config.from_object('settings')
app.secret_key = os.urandom(24)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

csrf = CSRFProtect(app)


@app.route('/', methods=['GET','POST'])
def index():

    # initiate the form..
    form = LoginValidation()

    if request.method in ('POST') :
        login_id = form.user_name_pid.data
        login_password = form.user_pid_Password.data

        # create a directory to hold the Logs
        login_msg = ldap_authentication(login_id, login_password)

        # validate the connection
        if login_msg == "Success":
            success_message = f"*** Authentication Success "
            flash(success_message)
            return redirect('/login/2fa/')

        else:
            error_message = f"*** Authentication Failed - {login_msg}"
            flash(error_message)
            return render_template('login.html', form=form)

    return render_template('login.html', form=form)


# 2FA page route
@app.route("/mfa/")
def mfa():
    # generating random secret key for authentication
    secret = pyotp.random_base32()
    return render_template("mfa.html", secret=secret)


# 2FA form route
@app.route("/login/2fa/", methods=["POST"])
def mfa_form():
    # getting secret key used by user
    secret = request.form.get("secret")
    # getting OTP provided by user
    otp = int(request.form.get("otp"))

    # verifying submitted OTP with PyOTP
    if pyotp.TOTP(secret).verify(otp):
        # inform users if OTP is valid
        flash("The TOTP 2FA token is valid", "success")
        return redirect(url_for("login_2fa"))
    else:
        # inform users if OTP is invalid
        flash("You have supplied an invalid 2FA token!", "danger")
        return redirect(url_for("login_2fa"))


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5000)