from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Users


UserInSchema = pydantic_model_creator(
    Users, name="UserIn",  exclude=["is_admin"], exclude_readonly=True
)
UserOutSchema = pydantic_model_creator(
    Users, name="UserOut", exclude=["password", "is_admin", "created_at", "modified_at"]
)
UserDatabaseSchema = pydantic_model_creator(
    Users, name="User", exclude=["created_at", "modified_at"]
)