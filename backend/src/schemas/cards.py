from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Cards


CardInSchema = pydantic_model_creator(
    Cards, name="CardIn", exclude=["id"], exclude_readonly=True)
CardOutSchema = pydantic_model_creator(
    Cards, name="Card"
)


class UpdateCard(BaseModel):    
    cardName : Optional[str]
    cardSet : Optional[str]
    cardRarity : Optional[str]
    cardType : Optional[str]
    cardSubType : Optional[str]
    cardClass : Optional[str]
    cardTwoSided : Optional[bool]
    cardFront : Optional[str]
    cardArt : Optional[str]
    # resource info
    cardPitchValue : Optional[int]
    cardRed : Optional[bool]
    cardYellow : Optional[bool]
    cardBlue : Optional[bool]
    # attack/defense
    cardAttack : Optional[int]
    cardDefense : Optional[int]
    # static keywords
    cardAB : Optional[int]
    cardABValue : Optional[int]
    cardBattleworn : Optional[bool]
    cardBladeBreak : Optional[bool]
    cardBloodDebt : Optional[bool]
    cardBoost : Optional[bool]    
    cardDominate : Optional[bool]
    cardGoAgain : Optional[bool]
    cardHeave : Optional[bool]
    cardHeaveValue : Optional[int]
    cardIntimidate : Optional[bool]
    cardLegendary : Optional[bool]
    cardOpt : Optional[bool]
    cardOptValue : Optional[int]
    cardPhantasm : Optional[bool]
    cardPierce : Optional[bool]
    cardQuell : Optional[bool]
    cardQuellValue : Optional[int]
    cardReload : Optional[bool]
    cardSpectra : Optional[bool]
    cardSpellvoid : Optional[bool]
    cardSpellvoidValue : Optional[int]
    cardTemper : Optional[bool]
    cardWard : Optional[bool]
    cardWardValue : Optional[int]
    # ability keywords   
    cardAttack : Optional[bool]
    cardAttackText : Optional[str]
    cardChannel : Optional[bool]
    cardChannelText : Optional[str]
    cardCombo : Optional[bool]
    cardComboText : Optional[str]
    cardContract : Optional[bool]
    cardContractText : Optional[str]
    cardCrush : Optional[bool]
    cardCrushText : Optional[str]
    cardEssence : Optional[bool]
    cardEssenceText : Optional[str]
    cardFusion : Optional[bool]
    cardFusionText : Optional[str]
    cardMaterial : Optional[bool]
    cardMaterialText : Optional[str]
    cardReprise : Optional[bool]
    cardRepriseText : Optional[str]
    cardRupture : Optional[bool]
    cardRuptureText : Optional[str]
    cardSpecialization : Optional[bool]
    cardSpecializationText : Optional[str]