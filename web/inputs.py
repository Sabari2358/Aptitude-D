from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField,validators, DateField

class Inputs(FlaskForm):
    number = IntegerField(label = 'Number',validators=[validators.DataRequired()])
    submit = SubmitField(label = 'Find')

class pandcInputs(FlaskForm):
    numbern = IntegerField(label = 'n (objects)',validators=[validators.DataRequired()])
    numberr = IntegerField(label = 'r (sample)',validators=[validators.DataRequired()])
    submit = SubmitField(label = 'Find')

class lcm_and_hcf(FlaskForm):
    values = StringField(label = 'Enter values seperated by space',validators=[validators.DataRequired()])
    submitL = SubmitField(label = 'Find LCM')
    submitH = SubmitField(label = 'Find HCF')

class year_input(FlaskForm):
    year = DateField(label='Year',validators=[validators.DataRequired()])
    submit = SubmitField(label = 'Find')

