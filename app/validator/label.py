from flask import current_app
from wtforms import StringField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Length, AnyOf

from app.utils.enums import LabelStatusEnum, LabelTypeEnum
from app.utils.errors import JsonError
from app.validator.base import BaseJsonValidator


class BaseLabelForm(BaseJsonValidator):
    name = StringField('name', validators=[DataRequired(message='该字段不可为空'), Length(max=50)])
    desc = StringField('desc', validators=[Length(max=150)])

    def format_error(self):
        errors = self.errors
        r = {k: ';'.join(errors[k]) for k in errors.keys()}
        return r


class CreateLabelForm(BaseLabelForm):
    cat = IntegerField(
        'cat', validators=[
            DataRequired(message='该字段不可为空'),
            AnyOf(LabelTypeEnum.cats(), message='不在可选范围')
        ]
    )
    status = IntegerField(
        'status', validators=[
            DataRequired(message='该字段不可为空'),
            AnyOf(LabelStatusEnum.valid_status(), message='不在可选范围')
        ]
    )

    def validate_cat(self, field):
        if field.data not in LabelTypeEnum.cats():
            raise JsonError(message=self.format_error())

    def validate_status(self, field):
        if field.data not in LabelStatusEnum.valid_status():
            raise JsonError(message=self.format_error())


class UpdateLabelForm(BaseLabelForm):

    id = IntegerField('id', validators=[DataRequired(message='该字段不可为空')])
    action = IntegerField('action', validators=[DataRequired(message='该字段不可为空'), AnyOf([1, 2])])
    cat = IntegerField('cat', validators=[])
    status = IntegerField('status', validators=[])

    def validate_cat(self, field):
        if not field.data:
            return
        if field.data not in LabelTypeEnum.cats():
            raise JsonError(message='不在可选范围')

    def validate_status(self, field):
        if not field.data:
            return
        if field.data not in LabelStatusEnum.valid_status():
            raise JsonError(message='不在可选范围')


