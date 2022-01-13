from enum import IntEnum


class LabelStatusEnum(IntEnum):
    DELETED = -1
    DRAFT = 0
    VALID = 1

    @classmethod
    def valid_status(cls):
        return [cls.VALID, cls.DRAFT]


class LabelTypeEnum(IntEnum):

    TAG = 1
    CATEGORY = 2

    @classmethod
    def cats(cls):
        return [cls.TAG, cls.CATEGORY]


