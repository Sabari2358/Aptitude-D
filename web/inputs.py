from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField,validators

class Inputs(FlaskForm):
    number = IntegerField(label = 'Number',validators=[validators.DataRequired()])
    submit = SubmitField(label = 'Find')

class pandcInputs(FlaskForm):
    numbern = IntegerField(label = 'n (objects)',validators=[validators.DataRequired()])
    numberr = IntegerField(label = 'r (sample)',validators=[validators.DataRequired()])
    submit = SubmitField(label = 'Find')

class lcm_and_hcf(FlaskForm):
    values = StringField(label = 'Enter values seperated by comma',validators=[validators.DataRequired()])
    submitL = SubmitField(label = 'Find LCM')
    submitH = SubmitField(label = 'Find HCF')

