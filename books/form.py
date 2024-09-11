from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,  FileField, DecimalField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, Length, InputRequired
from wtforms.validators import InputRequired
from app.models import Book

class BookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(2, 40)])
    description = StringField("Description", validators=[DataRequired(), Length(2, 100)])

    cover_photo = FileField("Cover_photo", validators=[DataRequired()])
    num_page= DecimalField('Num_page', validators=[InputRequired()])
        # SelectField("Num_page", validators=[DataRequired()]))
    submit = SubmitField("Save")