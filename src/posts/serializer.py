from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Post

class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        load_instance = True