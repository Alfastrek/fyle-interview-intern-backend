from marshmallow import EXCLUDE, fields, post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow_enum import EnumField
from core.models.assignments import Assignment, GradeEnum
from core.models.teachers import Teacher

class AssignmentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Assignment
        load_instance = True
        unknown = EXCLUDE

    class GeneralObjectSchema(SQLAlchemyAutoSchema):
        class Meta:
            fields = ("id", "teacher_id")

    id = fields.Integer(required=False, allow_none=True)
    content = fields.String()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    teacher_id = fields.Integer(dump_only=True)
    student_id = fields.Integer(dump_only=True)
    grade = fields.String(dump_only=True)
    state = fields.String(dump_only=True)

class AssignmentSubmitSchema(SQLAlchemyAutoSchema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Integer(required=True)
    teacher_id = fields.Integer(required=True)

class AssignmentGradeSchema(SQLAlchemyAutoSchema):
    class Meta:
        unknown = EXCLUDE

    id = fields.Integer(required=True)
    grade = EnumField(GradeEnum, required=True)

class TeacherSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher
        load_instance = True
        unknown = EXCLUDE

    id = fields.Integer(required=False, allow_none=True)
    user_id = fields.Integer(required=False, allow_none=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
