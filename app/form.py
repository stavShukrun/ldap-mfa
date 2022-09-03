from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Length


class LoginValidation(FlaskForm):
    user_name_pid = StringField('user_name_pid', validators=[DataRequired(), Length(min=2, max=20)],
                                render_kw={'autofocus': True, 'placeholder': 'Enter User'})

    user_pid_Password = PasswordField('user_pid_Password', validators=[DataRequired(), Length(min=2, max=20)],
                                render_kw={'autofocus': True, 'placeholder': 'Enter your login Password'})

class MfaVaValidation(FlaskForm):
    secret = StringField('secret', validators=[DataRequired(), Length(min=2, max=20)],
                                render_kw={'autofocus': True, 'placeholder': 'Enter User'})

    otp = StringField('otp', validators=[DataRequired(), Length(min=2, max=20)],
                                render_kw={'autofocus': True, 'placeholder': 'Enter User'})