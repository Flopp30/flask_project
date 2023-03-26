from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class UserLoginForm(FlaskForm):
    email = StringField(
        "Email Address",
        [
            validators.DataRequired(),
            validators.Email(),
            validators.Length(min=6, max=200),
        ],
        filters=[lambda data: data and data.lower()],
    )
    password = PasswordField(
        "Password",
        [
            validators.DataRequired(),
        ],
    )
    submit = SubmitField("Login")


class UserRegisterForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    email = StringField(
        "Email Address",
        [
            validators.DataRequired(),
            validators.Email(),
            validators.Length(min=6, max=200),
        ],
        filters=[lambda data: data and data.lower()],
    )
    password = PasswordField(
        "New Password",
        [
            validators.DataRequired(),
            validators.EqualTo("confirm_password", message="Passwords must match"),
        ],
    )
    confirm_password = PasswordField("Confirm password")
    submit = SubmitField("Register")
