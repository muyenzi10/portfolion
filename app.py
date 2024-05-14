from flask import Flask, render_template, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError
app = Flask(__name__)
# confifaration of mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///web2.db'
db = SQLAlchemy(app)
app.app_context().push()
app.config['SECRET_KEY'] = 'THismysquelsazn'
# class of label 
class LoginForm(FlaskForm):
    def validate_email(self, email_to_check):
        email= Client.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('email already exists! change email')
        else:
            print("correct")         
    name = StringField(label='Name:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email:', validators=[Email(), DataRequired()])
    date = StringField(label='Date:')
    submit= SubmitField(label='submit')
# class of create datebase    
class Client(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name  = db.Column(db.String(length=30), nullable=False)
    email = db.Column(db.String(length=30), nullable=False, unique=True)
    date  = db.Column(db.String(length=30), nullable=False)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')
@app.route("/packages")
def packages():
    return render_template('package.html')

@app.route("/book", methods=['GET', 'POST'])    
def book():
    form = LoginForm()
    if form.validate_on_submit():
        dt = Client(name=form.name.data,email=form.email.data,date=form.date.data)
        db.session.add(dt)
        db.session.commit()
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f"there was an error: {err_msg}", category='danger')
    return render_template('book.html', form=form)                
if __name__ == '__main__':
    app.run(debug=True)      