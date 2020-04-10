from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, TimeField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, EqualTo, Optional


class SendTaskForm(FlaskForm):
    num = StringField('Номер задачи', validators=[DataRequired()])
    answer = StringField('Ответ')

    image = FileField('Если требуется, прикрепите изображение')

    submit = SubmitField('Отправить')