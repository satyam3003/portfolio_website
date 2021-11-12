from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from flask_wtf.file import FileAllowed
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


class Exp(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    file = FileField("Upload Image", validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    body = CKEditorField("Blog Content")
    submit = SubmitField("Submit Post")


class Pro(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    file = FileField("Upload Image", validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    body = CKEditorField("Blog Content")
    link = StringField('Link', validators=[URL()])
    submit = SubmitField("Submit Post")


class Awa(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    file = FileField("Upload Image", validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    body = CKEditorField("Blog Content")
    link = StringField('Link', validators=[URL()])
    submit = SubmitField("Submit Post")


class Cert(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    file = FileField("Upload Image", validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    body = CKEditorField("Blog Content")
    link = StringField('Link', validators=[URL()])
    submit = SubmitField("Submit Post")
