from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "cards" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "cardName" VARCHAR(256) NOT NULL,
    "cardSet" VARCHAR(64) NOT NULL,
    "cardRarity" VARCHAR(64) NOT NULL,
    "cardType" VARCHAR(64) NOT NULL,
    "cardSubType" VARCHAR(64),
    "cardClass" VARCHAR(64),
    "cardTwoSided" BOOL NOT NULL  DEFAULT False,
    "cardFront" BOOL NOT NULL  DEFAULT True,
    "cardArt" VARCHAR(256),
    "cardWeaponType" VARCHAR(256),
    "cardHands" INT NOT NULL  DEFAULT 0,
    "cardPitchValue" INT NOT NULL  DEFAULT 0,
    "cardRed" BOOL NOT NULL  DEFAULT False,
    "cardYellow" BOOL NOT NULL  DEFAULT False,
    "cardBlue" BOOL NOT NULL  DEFAULT False,
    "cardAttack" INT NOT NULL  DEFAULT 0,
    "cardDefense" INT NOT NULL  DEFAULT 0,
    "cardAB" BOOL NOT NULL  DEFAULT False,
    "cardABValue" INT NOT NULL  DEFAULT 0,
    "cardBattleworn" BOOL NOT NULL  DEFAULT False,
    "cardBladeBreak" BOOL NOT NULL  DEFAULT False,
    "cardBloodDebt" BOOL NOT NULL  DEFAULT False,
    "cardBoost" BOOL NOT NULL  DEFAULT False,
    "cardDominate" BOOL NOT NULL  DEFAULT False,
    "cardGoAgain" BOOL NOT NULL  DEFAULT False,
    "cardHeave" BOOL NOT NULL  DEFAULT False,
    "cardHeaveValue" INT NOT NULL  DEFAULT 0,
    "cardIntimidate" BOOL NOT NULL  DEFAULT False,
    "cardLegendary" BOOL NOT NULL  DEFAULT False,
    "cardOpt" BOOL NOT NULL  DEFAULT False,
    "cardOptValue" INT NOT NULL  DEFAULT 0,
    "cardPhantasm" BOOL NOT NULL  DEFAULT False,
    "cardPierce" BOOL NOT NULL  DEFAULT False,
    "cardPierceVal" INT NOT NULL  DEFAULT 0,
    "cardQuell" BOOL NOT NULL  DEFAULT False,
    "cardQuellValue" INT NOT NULL  DEFAULT 0,
    "cardReload" BOOL NOT NULL  DEFAULT False,
    "cardSpectra" BOOL NOT NULL  DEFAULT False,
    "cardSpellvoid" BOOL NOT NULL  DEFAULT False,
    "cardSpellvoidValue" INT NOT NULL  DEFAULT 0,
    "cardTemper" BOOL NOT NULL  DEFAULT False,
    "cardWard" BOOL NOT NULL  DEFAULT False,
    "cardWardValue" INT,
    "cardAttackAct" BOOL NOT NULL  DEFAULT False,
    "cardAttackActText" TEXT,
    "cardAttackReact" BOOL NOT NULL  DEFAULT False,
    "cardAttackReactText" TEXT,
    "cardInstantAct" BOOL NOT NULL  DEFAULT False,
    "cardInstantActText" TEXT,
    "cardDefenseAct" BOOL NOT NULL  DEFAULT False,
    "cardDefenseActText" TEXT,
    "cardChannel" BOOL NOT NULL  DEFAULT False,
    "cardChannelText" TEXT,
    "cardCombo" BOOL NOT NULL  DEFAULT False,
    "cardComboText" TEXT,
    "cardContract" BOOL NOT NULL  DEFAULT False,
    "cardContractText" TEXT,
    "cardCrush" BOOL NOT NULL  DEFAULT False,
    "cardCrushText" TEXT,
    "cardEssence" BOOL NOT NULL  DEFAULT False,
    "cardEssenceText" TEXT,
    "cardFusion" BOOL NOT NULL  DEFAULT False,
    "cardFusionText" TEXT,
    "cardMaterial" BOOL NOT NULL  DEFAULT False,
    "cardMaterialText" TEXT,
    "cardReprise" BOOL NOT NULL  DEFAULT False,
    "cardRepriseText" TEXT,
    "cardRupture" BOOL NOT NULL  DEFAULT False,
    "cardRuptureText" TEXT,
    "cardSpecialization" BOOL NOT NULL  DEFAULT False,
    "cardSpecializationText" TEXT
);
CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "is_admin" BOOL NOT NULL  DEFAULT False,
    "username" VARCHAR(32) NOT NULL UNIQUE,
    "email" VARCHAR(50),
    "password" VARCHAR(128),
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "decks" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "deckName" VARCHAR(64) NOT NULL UNIQUE,
    "deckPublic" BOOL NOT NULL  DEFAULT True,
    "deckBlitz" BOOL NOT NULL  DEFAULT False,
    "deckList" TEXT,
    "deckCreator_id" INT NOT NULL REFERENCES "users" ("id") ON DELETE CASCADE,
    "deckHero_id" INT NOT NULL REFERENCES "cards" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
