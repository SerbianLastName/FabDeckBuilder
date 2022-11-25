from tortoise import fields, models

# from tortoise.contrib.pydantic import pydantic_model_creator


class Cards(models.Model):
    id = fields.IntField(pk=True)
    # basic info
    cardName = fields.CharField(max_length=256)
    cardSet = fields.CharField(max_length=64)
    cardRarity = fields.CharField(max_length=64)
    cardType = fields.CharField(max_length=64)
    cardSubType = fields.CharField(max_length=64, null=True, default=None)
    cardClass = fields.CharField(max_length=64)
    cardTwoSided = fields.BooleanField(default=False)
    cardFront = fields.BooleanField(default=True)
    cardArt = fields.CharField(max_length=256)
    cardWeaponType = fields.CharField(max_length=256)
    cardHands = fields.IntField(default=0)
    # resource info
    cardPitchValue = fields.IntField(default=0)
    cardRed = fields.BooleanField(default=False)
    cardYellow = fields.BooleanField(default=False)
    cardBlue = fields.BooleanField(default=False)
    # attack/defense
    cardAttack = fields.IntField(default=0)
    cardDefense = fields.IntField(default=0)
    # static keywords
    cardAB = fields.BooleanField(default=False)
    cardABValue = fields.IntField(default=0)
    cardBattleworn = fields.BooleanField(default=False)
    cardBladeBreak = fields.BooleanField(default=False)
    cardBloodDebt = fields.BooleanField(default=False)
    cardBoost = fields.BooleanField(default=False)
    cardDominate = fields.BooleanField(default=False)
    cardGoAgain = fields.BooleanField(default=False)
    cardHeave = fields.BooleanField(default=False)
    cardHeaveValue = fields.IntField(default=0)
    cardIntimidate = fields.BooleanField(default=False)
    cardLegendary = fields.BooleanField(default=False)
    cardOpt = fields.BooleanField(default=False)
    cardOptValue = fields.IntField(default=0)
    cardPhantasm = fields.BooleanField(default=False)
    cardPierce = fields.BooleanField(default=False)
    cardQuell = fields.BooleanField(default=False)
    cardQuellValue = fields.IntField(default=0)
    cardReload = fields.BooleanField(default=False)
    cardSpectra = fields.BooleanField(default=False)
    cardSpellvoid = fields.BooleanField(default=False)
    cardSpellvoidValue = fields.IntField(default=0)
    cardTemper = fields.BooleanField(default=False)
    cardWard = fields.BooleanField(default=False)
    cardWardValue = fields.IntField(null=True)
    # ability keywords
    cardAttack = fields.BooleanField(default=False)
    cardAttackText = fields.TextField(null=True)
    cardChannel = fields.BooleanField(default=False)
    cardChannelText = fields.TextField(null=True)
    cardCombo = fields.BooleanField(default=False)
    cardComboText = fields.TextField(null=True)
    cardContract = fields.BooleanField(default=False)
    cardContractText = fields.TextField(null=True)
    cardCrush = fields.BooleanField(default=False)
    cardCrushText = fields.TextField(null=True)
    cardEssence = fields.BooleanField(default=False)
    cardEssenceText = fields.TextField(null=True)
    cardFusion = fields.BooleanField(default=False)
    cardFusionText = fields.TextField(null=True)
    cardMaterial = fields.BooleanField(default=False)
    cardMaterialText = fields.TextField(null=True)
    cardReprise = fields.BooleanField(default=False)
    cardRepriseText = fields.TextField(null=True)
    cardRupture = fields.BooleanField(default=False)
    cardRuptureText = fields.TextField(null=True)
    cardSpecialization = fields.BooleanField(default=False)
    cardSpecializationText = fields.TextField(null=True)

    def __str__(self):
        return self.cardName


class Users(models.Model):
    id = fields.IntField(pk=True)
    is_admin = fields.BooleanField(default=False)
    username = fields.CharField(max_length=32, unique=True)
    email = fields.CharField(max_length=50, null=True)
    password = fields.CharField(max_length=128, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)


class Decks(models.Model):
    id = fields.IntField(pk=True)
    deckName = fields.CharField(max_length=64, unique=True)
    deckCreator = fields.ForeignKeyField("models.Users", related_name="deck")
    deckPublic = fields.BooleanField(default=True)
    deckBlitz = fields.BooleanField(default=False)
    deckList = fields.TextField()
