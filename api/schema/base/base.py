"""Base marshmallow schemas"""
from marshmallow import Schema, fields

from api.utilities.validators.base import ValidationError


class BaseSchema(Schema):
    """Base marshmallow schemas with common attributes"""
    id = fields.String(dump_only=True)
    created_at = fields.DateTime(dump_only=True, dump_to='createdAt')
    updated_at = fields.DateTime(dump_only=True, dump_to='updatedAt')

    def load_object_into_schema(self, data, partial=False):
        """Helper function to load python objects into schemas"""
        data, errors = self.load(data, partial=partial)

        if errors:
            raise ValidationError(
                dict(errors=errors, message='An error occurred'), 400)

        return data
