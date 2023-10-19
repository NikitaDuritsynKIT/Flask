from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models import Post

class PostSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        load_instance = True