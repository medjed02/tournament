from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, TimeField
from wtforms.validators import DataRequired, EqualTo, Optional


class GetTaskForm(FlaskForm):
    num_task = SelectField('Выберите задачу', validators=[Optional()])
    submit = SubmitField('Получить задачу')