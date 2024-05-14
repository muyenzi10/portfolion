from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
# field of label 
class Reg(FlaskForm):
    name = StringField(label='username')
    email= StringField(label='Email')
    email= StringField(label='date')
    submit= SubmitField(label='submit')