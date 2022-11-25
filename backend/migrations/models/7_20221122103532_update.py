from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "decklist" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "deckID_id" INT NOT NULL REFERENCES "decks" ("id") ON DELETE CASCADE
);;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "decklist";"""
