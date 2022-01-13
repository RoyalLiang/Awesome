from datetime import datetime

from flask import jsonify, request
from loguru import logger

from app.models import LabelModel
from app.utils.base import json_response
from app.utils.db import db
from app.utils.enums import LabelStatusEnum
from app.utils.redprint import RedPrint
from app.validator.label import CreateLabelForm, UpdateLabelForm

label_api = RedPrint("label")


@label_api.route('/createLabel', methods=['POST'])
def create_label():
    label_form = CreateLabelForm()
    logger.info(f"get create label req: {request.json}")
    if label_form.validate():
        exist_label = LabelModel.query.filter(
            LabelModel.cat == label_form.cat.data, LabelModel.name == label_form.name.data, LabelModel.status == 1
        ).first()
        if exist_label:
            return json_response(1, msg='已存在相同标签')
        with db.auto_commit():
            LabelModel.create(**request.json)
        return jsonify({"result": 0})
    return jsonify({"result": 1})


@label_api.route('/labelList', methods=['GET'])
def get_label_list():
    labels = LabelModel.query.filter(LabelModel.status == LabelStatusEnum.VALID)
    label = [{
        'id': i.id,
        'name': i.name,
        'cat': i.cat,
        'desc': i.desc,
    } for i in labels]
    return json_response(0, data=label)


@label_api.route('/updateLabel', methods=['POST'])
def update_label():
    form = UpdateLabelForm()
    if form.validate():
        label = LabelModel.query.filter(LabelModel.id == form.id.data).first()
        if not label:
            return json_response(-1, msg='未查询到当前标签')
        with db.auto_commit():
            body = request.json
            body['update_time'] = datetime.now()
            label.update(**body)
        return json_response()
