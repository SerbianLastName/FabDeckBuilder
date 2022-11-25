from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "cards" ALTER COLUMN "cardComboText" TYPE TEXT USING "cardComboText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardComboText" TYPE TEXT USING "cardComboText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardComboText" TYPE TEXT USING "cardComboText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardRepriseText" TYPE TEXT USING "cardRepriseText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardRepriseText" TYPE TEXT USING "cardRepriseText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardRepriseText" TYPE TEXT USING "cardRepriseText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardAttackText" TYPE TEXT USING "cardAttackText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardAttackText" TYPE TEXT USING "cardAttackText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardAttackText" TYPE TEXT USING "cardAttackText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardRuptureText" TYPE TEXT USING "cardRuptureText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardRuptureText" TYPE TEXT USING "cardRuptureText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardRuptureText" TYPE TEXT USING "cardRuptureText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardChannelText" TYPE TEXT USING "cardChannelText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardChannelText" TYPE TEXT USING "cardChannelText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardChannelText" TYPE TEXT USING "cardChannelText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardContractText" TYPE TEXT USING "cardContractText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardContractText" TYPE TEXT USING "cardContractText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardContractText" TYPE TEXT USING "cardContractText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardMaterialText" TYPE TEXT USING "cardMaterialText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardMaterialText" TYPE TEXT USING "cardMaterialText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardMaterialText" TYPE TEXT USING "cardMaterialText"::TEXT;
        CREATE TABLE IF NOT EXISTS "decks" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "deckName" VARCHAR(64) NOT NULL UNIQUE,
    "deckPublic" BOOL NOT NULL  DEFAULT True,
    "deckCreator_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE
);;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "cards" ALTER COLUMN "cardComboText" TYPE VARCHAR(512) USING "cardComboText"::VARCHAR(512);
        ALTER TABLE "cards" ALTER COLUMN "cardComboText" TYPE VARCHAR(512) USING "cardComboText"::VARCHAR(512);
        ALTER TABLE "cards" ALTER COLUMN "cardComboText" TYPE VARCHAR(512) USING "cardComboText"::VARCHAR(512);
        ALTER TABLE "cards" ALTER COLUMN "cardRepriseText" TYPE VARCHAR(512) USING "cardRepriseText"::VARCHAR(512);
        ALTER TABLE "cards" ALTER COLUMN "cardRepriseText" TYPE VARCHAR(512) USING "cardRepriseText"::VARCHAR(512);
        ALTER TABLE "cards" ALTER COLUMN "cardRepriseText" TYPE VARCHAR(512) USING "cardRepriseText"::VARCHAR(512);
        ALTER TABLE "cards" ALTER COLUMN "cardAttackText" TYPE VARCHAR(512) USING "cardAttackText"::VARCHAR(512);
        ALTER TABLE "cards" ALTER COLUMN "cardAttackText" TYPE VARCHAR(512) USING "cardAttackText"::VARCHAR(512);
        ALTER TABLE "cards" ALTER COLUMN "cardAttackText" TYPE VARCHAR(512) USING "cardAttackText"::VARCHAR(512);
        ALTER TABLE "cards" ALTER COLUMN "cardRuptureText" TYPE VARCHAR(512) USING "cardRuptureText"::VARCHAR(512);
        ALTER TABLE "cards" ALTER COLUMN "cardRuptureText" TYPE VARCHAR(512) USING "cardRuptureText"::VARCHAR(512);
        ALTER TABLE "cards" ALTER COLUMN "cardRuptureText" TYPE VARCHAR(512) USING "cardRuptureText"::VARCHAR(512);
        ALTER TABLE "cards" ALTER COLUMN "cardChannelText" TYPE VARCHAR(512) USING "cardChannelText"::VARCHAR(512);
        ALTER TABLE "cards" ALTER COLUMN "cardChannelText" TYPE VARCHAR(512) USING "cardChannelText"::VARCHAR(512);
        ALTER TABLE "cards" ALTER COLUMN "cardChannelText" TYPE VARCHAR(512) USING "cardChannelText"::VARCHAR(512);
        ALTER TABLE "cards" ALTER COLUMN "cardContractText" TYPE VARCHAR(512) USING "cardContractText"::VARCHAR(512);
        ALTER TABLE "cards" ALTER COLUMN "cardContractText" TYPE VARCHAR(512) USING "cardContractText"::VARCHAR(512);
        ALTER TABLE "cards" ALTER COLUMN "cardContractText" TYPE VARCHAR(512) USING "cardContractText"::VARCHAR(512);
        ALTER TABLE "cards" ALTER COLUMN "cardMaterialText" TYPE VARCHAR(512) USING "cardMaterialText"::VARCHAR(512);
        ALTER TABLE "cards" ALTER COLUMN "cardMaterialText" TYPE VARCHAR(512) USING "cardMaterialText"::VARCHAR(512);
        ALTER TABLE "cards" ALTER COLUMN "cardMaterialText" TYPE VARCHAR(512) USING "cardMaterialText"::VARCHAR(512);
        DROP TABLE IF EXISTS "decks";"""
