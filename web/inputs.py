from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField,validators

class Inputs(FlaskForm):
    number = IntegerField(label = 'Number',validators=[validators.DataRequired()])
    submit = SubmitField(label = 'Find')

class pandcInputs(FlaskForm):
    numbern = IntegerField(label = 'n (objects)',validators=[validators.DataRequired()])
    numberr = IntegerField(label = 'r (sample)',validators=[validators.DataRequired()])
    submit = SubmitField(label = 'Find')