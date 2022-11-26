from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "cards" RENAME COLUMN "cardPierceVal" TO "cardPierceValue";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "cards" RENAME COLUMN "cardPierceValue" TO "cardPierceVal";"""
