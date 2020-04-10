from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField, TimeField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, EqualTo, Optional


class TournamentForm(FlaskForm):
    name = StringField('Название соревнования', validators=[DataRequired()])
    type_of_tournament = SelectField('Тип соревнования', validators=[Optional()])

    time = TimeField('Введите длительность соревнования (часы:минуты)', validators=[DataRequired()])
    num_of_tasks = IntegerField('Введите количество экземпляров каждой задачи', validators=[DataRequired()])
    text = FileField('Прикрепите файл с задачами', validators=[FileRequired()])
    answers = FileField('Прикрепите файл с ответами к задачам с автоматической проверкой',
                        validators=[FileRequired()])

    submit = SubmitField('Создать соревнование')