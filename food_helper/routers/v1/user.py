from fastapi import APIRouter

from food_helper.core.dependencies.fastapi import DatabaseDependency, TokenDataDependency
from food_helper.lib.db import user as user_db
from food_helper.lib.schemas.user import UserCreateSchema, UserSchema


router = APIRouter(tags=["user"], prefix="/users")


@router.post("/", response_model=UserSchema)
async def create_user(db: DatabaseDependency, schema: UserCreateSchema) -> UserSchema:
    return await user_db.create_user(db, schema=schema)


@router.get("/me", response_model=UserSchema)
async def get_user(db: DatabaseDependency, token_data: TokenDataDependency) -> UserSchema:
    return await user_db.get_user(db, user_id=token_data.user_id)


@router.delete("/me", status_code=204)
async def delete_user(db: DatabaseDependency, token_data: TokenDataDependency) -> None:
    return await user_db.delete_user(db, user_id=token_data.user_id)
