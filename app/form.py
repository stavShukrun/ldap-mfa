from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Length


class LoginValidation(FlaskForm):
    user_name = StringField('user_name', validators=[DataRequired(), Length(min=2, max=20)],
                                render_kw={'autofocus': True, 'placeholder': 'Enter User'})

    user_Password = PasswordField('user_Password', validators=[DataRequired(), Length(min=2, max=20)],
                                render_kw={'autofocus': True, 'placeholder': 'Enter your login Password'})

class MfaVaValidation(FlaskForm):
    secret = StringField('secret', validators=[DataRequired(), Length(min=2, max=20)],
                                render_kw={'autofocus': True, 'placeholder': 'Enter User'})

    otp = StringField('otp', validators=[DataRequired(), Length(min=2, max=20)],
                                render_kw={'autofocus': True, 'placeholder': 'Enter User'})