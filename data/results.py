import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class UserResult(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'results'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    cnt_points = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    attempts = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    cnt_tasks = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    tasks = sqlalchemy.Column(sqlalchemy.String, nullable=True)
