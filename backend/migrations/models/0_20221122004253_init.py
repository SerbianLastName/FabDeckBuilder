from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "fabcard" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "cardName" VARCHAR(256) NOT NULL,
    "cardSet" VARCHAR(64) NOT NULL,
    "cardType" VARCHAR(64) NOT NULL,
    "cardSubType" VARCHAR(64),
    "cardClass" VARCHAR(64) NOT NULL,
    "cardTwoSided" BOOL NOT NULL  DEFAULT False,
    "cardFront" BOOL NOT NULL  DEFAULT True,
    "cardArt" VARCHAR(256) NOT NULL,
    "cardPitchValue" INT NOT NULL  DEFAULT 0,
    "cardRed" BOOL NOT NULL  DEFAULT False,
    "cardYellow" BOOL NOT NULL  DEFAULT False,
    "cardBlue" BOOL NOT NULL  DEFAULT False,
    "cardAttack" BOOL NOT NULL  DEFAULT False,
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
    "cardQuell" BOOL NOT NULL  DEFAULT False,
    "cardQuellValue" INT NOT NULL  DEFAULT 0,
    "cardReload" BOOL NOT NULL  DEFAULT False,
    "cardSpectra" BOOL NOT NULL  DEFAULT False,
    "cardSpellvoid" BOOL NOT NULL  DEFAULT False,
    "cardSpellvoidValue" INT NOT NULL  DEFAULT 0,
    "cardTemper" BOOL NOT NULL  DEFAULT False,
    "cardWard" BOOL NOT NULL  DEFAULT False,
    "cardWardValue" INT,
    "cardAttackText" VARCHAR(512),
    "cardChannel" BOOL NOT NULL  DEFAULT False,
    "cardChannelText" VARCHAR(512),
    "cardCombo" BOOL NOT NULL  DEFAULT False,
    "cardComboText" VARCHAR(512),
    "cardContract" BOOL NOT NULL  DEFAULT False,
    "cardContractText" VARCHAR(512),
    "cardCrush" BOOL NOT NULL  DEFAULT False,
    "cardEssence" BOOL NOT NULL  DEFAULT False,
    "cardEssenceText" VARCHAR(128),
    "cardFusion" BOOL NOT NULL  DEFAULT False,
    "cardFusionText" VARCHAR(128),
    "cardMaterial" BOOL NOT NULL  DEFAULT False,
    "cardMaterialText" VARCHAR(512),
    "cardReprise" BOOL NOT NULL  DEFAULT False,
    "cardRepriseText" VARCHAR(512),
    "cardRupture" BOOL NOT NULL  DEFAULT False,
    "cardRuptureText" VARCHAR(512),
    "cardSpecialization" BOOL NOT NULL  DEFAULT False,
    "cardSpecializationText" VARCHAR(128)
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
