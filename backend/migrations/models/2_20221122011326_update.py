from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "fabcard" RENAME COLUMN "id" TO "card_id";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "fabcard" RENAME COLUMN "card_id" TO "id";"""
