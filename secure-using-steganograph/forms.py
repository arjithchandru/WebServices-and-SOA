from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField,TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed
class encodeForm(FlaskForm):
	picture = FileField(validators = [DataRequired(), FileAllowed(['png'])])
	text = TextAreaField('Enter your text:', validators = [DataRequired()])
	submit = SubmitField('submit')
class decodeForm(FlaskForm):
	picture_o = FileField(validators = [DataRequired(), FileAllowed(['png'])])
	picture_e = FileField(validators = [DataRequired(), FileAllowed(['png'])])
	pwd_d = IntegerField('Pixel length:', validators = [DataRequired(message="Provided pixel length is not alphanumeric. Please check the password again!")])
	submit_d = SubmitField('submit')
