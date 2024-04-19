from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import EXCLUDE

class TeacherSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher
        load_instance = True
        unknown = EXCLUDE

    id = auto_field(required=False, allow_none=True)
    user_id = auto_field(required=False, allow_none=True)
    created_at = auto_field(dump_only=True)
    updated_at = auto_field(dump_only=True)

    def handle_error(self, error, data):
        """Handle any errors during deserialization."""
        raise ValueError(f"An error occurred during deserialization: {error}")

