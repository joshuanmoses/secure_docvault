# web/xforms.py

from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired

class UploadDocumentForm(FlaskForm):
    folder = StringField('Folder Name', validators=[DataRequired()])
    file = FileField('Upload Document', validators=[DataRequired()])
    submit = SubmitField('Upload')

class CreateFolderForm(FlaskForm):
    folder_name = StringField('New Folder Name', validators=[DataRequired()])
    submit = SubmitField('Create Folder')

class SearchForm(FlaskForm):
    query = StringField('Search Documents', validators=[DataRequired()])
    submit = SubmitField('Search')
