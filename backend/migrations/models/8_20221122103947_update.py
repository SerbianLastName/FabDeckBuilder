from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "cards" ALTER COLUMN "cardEssenceText" TYPE TEXT USING "cardEssenceText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardEssenceText" TYPE TEXT USING "cardEssenceText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardEssenceText" TYPE TEXT USING "cardEssenceText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardFusionText" TYPE TEXT USING "cardFusionText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardFusionText" TYPE TEXT USING "cardFusionText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardFusionText" TYPE TEXT USING "cardFusionText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardSpecializationText" TYPE TEXT USING "cardSpecializationText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardSpecializationText" TYPE TEXT USING "cardSpecializationText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardSpecializationText" TYPE TEXT USING "cardSpecializationText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardCrushText" TYPE TEXT USING "cardCrushText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardCrushText" TYPE TEXT USING "cardCrushText"::TEXT;
        ALTER TABLE "cards" ALTER COLUMN "cardCrushText" TYPE TEXT USING "cardCrushText"::TEXT;
        ALTER TABLE "decks" ADD "deckList" TEXT NOT NULL;
        DROP TABLE IF EXISTS "decklist";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "cards" ALTER COLUMN "cardEssenceText" TYPE VARCHAR(128) USING "cardEssenceText"::VARCHAR(128);
        ALTER TABLE "cards" ALTER COLUMN "cardEssenceText" TYPE VARCHAR(128) USING "cardEssenceText"::VARCHAR(128);
        ALTER TABLE "cards" ALTER COLUMN "cardEssenceText" TYPE VARCHAR(128) USING "cardEssenceText"::VARCHAR(128);
        ALTER TABLE "cards" ALTER COLUMN "cardFusionText" TYPE VARCHAR(128) USING "cardFusionText"::VARCHAR(128);
        ALTER TABLE "cards" ALTER COLUMN "cardFusionText" TYPE VARCHAR(128) USING "cardFusionText"::VARCHAR(128);
        ALTER TABLE "cards" ALTER COLUMN "cardFusionText" TYPE VARCHAR(128) USING "cardFusionText"::VARCHAR(128);
        ALTER TABLE "cards" ALTER COLUMN "cardSpecializationText" TYPE VARCHAR(128) USING "cardSpecializationText"::VARCHAR(128);
        ALTER TABLE "cards" ALTER COLUMN "cardSpecializationText" TYPE VARCHAR(128) USING "cardSpecializationText"::VARCHAR(128);
        ALTER TABLE "cards" ALTER COLUMN "cardSpecializationText" TYPE VARCHAR(128) USING "cardSpecializationText"::VARCHAR(128);
        ALTER TABLE "cards" ALTER COLUMN "cardCrushText" TYPE VARCHAR(128) USING "cardCrushText"::VARCHAR(128);
        ALTER TABLE "cards" ALTER COLUMN "cardCrushText" TYPE VARCHAR(128) USING "cardCrushText"::VARCHAR(128);
        ALTER TABLE "cards" ALTER COLUMN "cardCrushText" TYPE VARCHAR(128) USING "cardCrushText"::VARCHAR(128);
        ALTER TABLE "decks" DROP COLUMN "deckList";"""
