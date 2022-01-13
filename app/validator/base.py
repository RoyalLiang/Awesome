from flask import current_app, request
from wtforms import Form, StringField
from wtforms.validators import DataRequired, Length


class BaseJsonValidator(Form):
    def __init__(self):
        body_data = request.json
        query_data = request.args.to_dict()
        super(BaseJsonValidator, self).__init__(**body_data, **query_data)

    def validate(self, **kwargs):
        passed = super(BaseJsonValidator, self).validate()
        if passed:
            return True
        else:
            raise ValueError(self.errors)

