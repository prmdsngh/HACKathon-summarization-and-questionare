
from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField,SelectField

from wtforms import validators, ValidationError


class pdfFileForm(Form):
   name = TextField("Name Of Student",[validators.Required("Please enter your name.")])